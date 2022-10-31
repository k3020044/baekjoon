# 최소일 = 최단 경로 길이 = BFS
# pop(0) 시간복잡도 O(n)이기 때문에 deque 사용
from collections import deque

M, N= map(int, input().split()) # m: 가로, n: 세로
arr = [list(map(int, input().split())) for _ in range(N)]
# 토마토 좌표 넣을 queue 생성
queue = deque([])

# visited 방문 queue에 넣기 = 익은 토마토 좌표 queue에 추가
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])

#     상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def bfs():
    # queue에 요소 있는 동안 반복 = 익은 토마토 있는 동안 반복
    while queue:
        x, y = queue.popleft()
        # 가능한 4방향 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 좌표안에 있으면서 안익은 토마토인 경우
            if 0 <= nx < N  and 0 <= ny < M and arr[nx][ny] == 0:
                # 길이 표시하기 위해 +1
                arr[nx][ny] = arr[x][y] + 1
                # 새롭게 익은 토마토 queue에 추가
                queue.append([nx, ny])

bfs() # 함수 호출
for i in arr:
    for j in i:
        # 안익은 토마토 1개라도 있으면 실패
        if j == 0:
            print(-1)
            exit()
    # 1차원 리스트 순회하면서 max값 갱신되도록        
    cnt = max(cnt, max(i))
print(cnt - 1)