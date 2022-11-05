# 최소일 = 최단 경로 길이 = BFS
from collections import deque

N, K = map(int, input().split()) # n:행열크기, k: 자연수
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 바이러스 (시간, 값, x좌표, y좌표) 넣을 리스트 생성
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append([0, arr[i][j], i, j])

# value 값 기준으로 오름차순 정렬, 낮은거부터 전염되기 때문에
# deque는 sort가 안되기때문에, 임의의 리스트에서 sort후 deque로 벼환
virus.sort(key=lambda x: x[1])
queue = deque(virus)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    time, value, x, y = queue.popleft()
    # 가지치기, 답에서 원하는 시간 이후로는 구할 필요 없음
    if time == S:
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
            arr[nx][ny] = value
            queue.append([time+1, value, nx, ny])

print(arr[X-1][Y-1])