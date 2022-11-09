arr = [list(map(int, input().split())) for _ in range(5)]
check = [list(map(int, input().split())) for _ in range(5)]

def bingo(cnt):
    # 빙고 체크
    bingo = 0
    #가로, 세로
    for i in range(5):
        if arr[i] == [0, 0, 0, 0, 0]:
            bingo += 1

        lst = []
        for j in range(5):
            lst.append(arr[j][i])
            if lst == [0, 0, 0, 0, 0]:
                bingo += 1

    #대각선
    lst1 = []
    lst2 = []
    for i in range(5):
        lst1.append(arr[i][4-i]) # 오른쪽 대각선
        if lst1 == [0, 0, 0, 0, 0]:
            bingo += 1

    for i in range(5):
        lst2.append(arr[i][i]) # 왼쪽 대각선       
        if lst2 == [0, 0, 0, 0, 0]:
            bingo += 1

    if bingo >= 3:
        print(cnt)
        exit()

cnt = 0
for i in range(5):
    for j in range(5):
        for n in range(5):
            for m in range(5):
                if check[i][j] == arr[n][m]:
                    arr[n][m] = 0
                    cnt += 1
                    #print(arr)
                    bingo(cnt)