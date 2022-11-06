from collections import deque
import sys
input = sys.stdin.readline

# bfs 연합되는지 검사할 x좌표, y좌표 argument로 넣음
def bfs(i, j):
	# 큐 생성하고 검사할 좌표 넣음
	queue = deque()
	queue.append([i, j])
	# 큐는 pop해야하므로, 연합국 저장할 별도의 리스트 만듦
	united = []
	united.append([i, j])
	while queue:
		x, y = queue.popleft()
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			# 좌표안에 있고, 방문안했고, value 값차이 L이상 R이하인 경우
			if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
				if L <= abs(arr[nx][ny]-arr[x][y]) <= R:
					# 방문표시하고, 큐, united 리스트에 추가
					visited[nx][ny] = 1
					queue.append([nx, ny])
					united.append([nx, ny])
    # queue 검사 다 한경우 united 반환
	return united
N, L, R = map(int, input().split()) # N:행렬길이, L:최소차이, R:최대 차이
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 날짜 셀 변수
cnt = 0
# break 조건 : 인구이동이 더이상 발생하지 않는 경우
while True:
    # 방문표시 배열 생성
    visited = [[0] * N for _ in range(N+1)]
    # 인구이동이 일어났는지 체크할 변수 생성
    isMove = False
    for i in range(N):
        for j in range(N):
            # 방문안한 경우, 방문표시하고 bfs 호출하여 united 리스트 구함
            if visited[i][j] == 0:
                visited[i][j] = 1
                united = bfs(i, j)
                # 연합이 형성된 경우(=리스트 요소 2개이상인 경우) 값 변경
                if len(united) > 1:
                    # 인구 이동이 발생함 체크
                    isMove = True
                    num = sum([arr[x][y] for x, y in united]) // len(united)
                    for x, y in united:
                        arr[x][y] = num
    # 인구 이동이 더이상 일어나지 않으면 break
    if not isMove:
        break
    # 배열 for문으로 다 돌아서 united 체크한 후에 날짜 +1
    cnt += 1
print(cnt)