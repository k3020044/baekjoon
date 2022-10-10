arr = [[0] * 7 for _ in range(2)]
n, k = map(int, input().split()) # n: 학생수, k: 한방 최대 인원수
for _ in range(n):
    gender, grade = map(int, input().split())
    arr[gender][grade] += 1

cnt = 0 # 필요한 방개수
for i in range(2):
    for j in range(1, 7):
        if arr[i][j] % k == 0:
            cnt += arr[i][j] // k
        else:
            cnt += (arr[i][j] // k) + 1

print(cnt)