n = int(input())
# idx 값 맞추기 위해 0번에 미지값 추가
bulbs = [-1] + list(map(int, input().split()))
k = int(input())
students = [tuple(map(int, input().split())) for _ in range(k)]

for sex, num in students:
    # 성별이 남자일때
    if sex == 1:
        for i in range(num, n+1, num):
            bulbs[i] = 1 - bulbs[i]
    # 성별이 여자일때
    else:
        bulbs[num] = 1 - bulbs[num]
        for k in range(n//2):
            if num + k > n or num - k < 1: break
            if bulbs[num+k] == bulbs[num-k]:
                bulbs[num+k] = 1 - bulbs[num+k]
                bulbs[num-k] = 1 - bulbs[num-k]
            else:
                break  

for i in range(1, n+1):
    print(bulbs[i], end=' ')
    if i % 20 == 0:
        print()