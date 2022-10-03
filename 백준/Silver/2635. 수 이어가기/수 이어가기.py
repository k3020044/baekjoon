n = int(input())
max_length = 0
max_lst = []

for i in range(n//2, n+1):
    lst = [n] # i가 바뀔때마다 초기화되도록
    lst.append(i)
    x = 0 # 초기화 위치 주의!
    while x >= 0:
        x = lst[-2] - lst[-1]
        #print(x)
        if x >= 0:
            lst.append(x)
    if len(lst) > max_length:
        max_length = len(lst)
        max_lst = lst

print(max_length)
print(*max_lst)