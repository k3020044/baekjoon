from collections import deque

M, N, H = map(int, input().split()) # m: 가로, n: 세로, h: 층
# 토마토 좌표 넣을 queue 생성
queue = deque([])
# 3차원 배열 생성
box = []

# 3차원 배열 받기
for i in range(H): #층
    arr = []
    for j in range(N): #행
        arr.append(list(map(int, input().split())))
        for k in range(M): #열
            if arr[j][k] == 1:
                # 익은 토마토 좌표 (층, 행, 열) queue에 추가
                queue.append([i, j, k])
    # 2차원 배열 arr box에 append하여 3차원 배열 만들기
    box.append(arr)

#    위 아래 상 하 좌 우
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
cnt = 0

def bfs():
    # queue에 요소 있는 동안 반복 = 익은 토마토 있는 동안 반복
    while queue:
        x, y, z = queue.popleft()
        # 가능한 6방향 탐색
        for i in range(6):
            nx = x + dx[i] #층
            ny = y + dy[i] #행
            nz = z + dz[i] #열
            # 좌표안에 있으면서 안익은 토마토인 경우
            if 0 <= nx < H  and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
                # 길이 표시하기 위해 +1
                box[nx][ny][nz] = box[x][y][z] + 1
                # 새롭게 익은 토마토 queue에 추가
                queue.append([nx, ny, nz])

bfs() # 함수 호출
for i in box:
    for j in i:
        for k in j:
            # 안익은 토마토 1개라도 있으면 실패
            if k == 0:
                print(-1)
                exit()
        # 1차원 리스트 순회하면서 max값 갱신되도록
        cnt = max(cnt, max(j))
print(cnt - 1)