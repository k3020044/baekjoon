N = int(input())
lst = list(map(int, input().split())) # 학생들이 뽑은 번호 리스트
line = [0] * N # 학생들 줄 저장할 리스트
# print(lst)
for i in range(N):
    # 새로 삽입하는 위치에 이미 숫자가 있는 경우 앞으로 한칸씩 땡겨야함
    if line[-1-lst[i]] != 0:
        for j in range(-N, -lst[i]):
            line[j] = line[j+1]
        line[-1-lst[i]] = i+1
        # print(line)
    # 새로 삽입하는 위치에 숫자 없으면 바로 삽입
    else:
        line[-1-lst[i]] = i+1
        # print(line)
print(*line)