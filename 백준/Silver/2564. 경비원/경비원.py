n, m = map(int, input().split())
a = int(input()) # 상점 수
lst = [0] * a
for i in range(a):
    x, y = map(int, input().split()) # 상점 좌표
    if x == 1:
        lst[i] = y
    elif x == 2:
        lst[i] = n + m + (n - y)
    elif x == 3:
        lst[i] = n + m + n + (m - y)
    else:
        lst[i] = n + y
#print(lst)
i, j = map(int, input().split())
person = 0
if i == 1:
    person = j
elif i == 2:
    person = n + m + (n - j)
elif i == 3:
    person = n + m + n + (m - j)
else:
    person = n + j
#print(person)
min_sum = 0
for i in lst:
    if abs(i - person) <= n+m:
        min_sum += abs(i - person)
    else:
        min_sum += 2*(n + m) - abs(i - person)
print(min_sum)