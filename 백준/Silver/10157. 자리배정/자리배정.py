c, r = map(int, input().split()) # c가로, r세로
k = int(input())
if c*r < k:
    print(0)
    exit()
if k == 1:
    print(1, 1)
arr = [[0] * (c+1) for _ in range(r+1)]

# 시작점
x = r
y = 1
i = 0 # 방향
cnt = 1 # 1씩 증가하며 입력
arr[x][y] = 1

    # 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while cnt < k:
    #for i in range(4): # 이거는 한칸씩 방향바꾸면서 이동할때
    nx = x+dx[i]
    ny = y+dy[i]
    if 1<=nx<r+1 and 1<=ny<c+1 and arr[nx][ny] == 0:
        x = nx
        y = ny
        cnt += 1
        arr[x][y] = cnt
        if arr[x][y] == k:
            print(y, r - x + 1)
    else:
        i = (i+1) % 4 #방향전환