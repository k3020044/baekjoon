# 9개의 숫자를 리스트로 받음
lst = []
for _ in range(9):
    lst.append(int(input()))
# 리스트를 오름차순 정렬함
lst.sort()

# 9개중 2개를 선택하여, 나머지 7개의 원소 합이 100이면
# lst2에 append함. 이렇게한 이유는 여러가지 경우가 있는 경우 하나만 출력하게 하기위해
for i in range(8): #0~7까지
    for j in range(i+1, 9): #7까지
        if sum(lst) - lst[i] - lst[j] == 100:
            lst2 = []
            for k in range(9):
                if k != i and k != j:
                    lst2.append(lst[k])
for i in range(7):
    print(lst2[i])