arr = [[0]*101 for _ in range(101)]
for _ in range(4):
    x, y, n, m = map(int, input().split())

    for i in range(x, n):
        for j in range(y, m):
            arr[i][j] = '!'
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == '!':
            cnt += 1

print(cnt)