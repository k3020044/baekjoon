# DFS
N, M = map(int, input().split()) # N:행, M:열
arr = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)] # 울타리 설치한 뒤의 배열 저장을 위한 리스트

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0 # 정답 변수

# DFS로 각 바이러스가 사방으로 퍼지도록 하기, 바이러스의 (x, y) 좌표 argument
def virus(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 좌표 안에 있으면서 바이러스 전파할 수 있는 경우
        if 0<=nx<N and 0<=ny<M and temp[nx][ny] == 0:
            # 해당 위치에 바이러스 전파하고, 다시 재귀적으로 수행
            temp[nx][ny] = 2
            virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 함수
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS로 울타리 설치하는 모든 경우 탐색
def dfs(count):
    global answer
    # 2. 울타리가 3개 설치된 경우 바이러스 전파
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = arr[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        answer = max(answer, get_score())
        return
    # 울타리 설치하는 모든 경우의 수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count += 1
                dfs(count)
                arr[i][j] = 0
                count -= 1

dfs(0)
print(answer)