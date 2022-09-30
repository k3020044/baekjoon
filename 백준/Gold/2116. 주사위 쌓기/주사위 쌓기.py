n = int(input())
lst = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n-1)]

# 맞은편 인덱스 찾는 함수
def find_index(x):
	if x == 0:
		return 5
	if x == 1:
		return 3
	if x == 2:
		return 4
	if x == 3:
		return 1
	if x == 4:
		return 2
	if x == 5:
		return 0

max_sum = 0

for i in range(6):
    down = lst[i]
    up = lst[find_index(i)]
    sum_value = 0
    #print(down, up)
    if down == 6 or up == 6:
        if down == 5 or up == 5:
            sum_value += 4
        else:
            sum_value += 5
    else:
        sum_value += 6
    #print(lst)
    for j in range(n-1):
        down = up
        up = arr[j][find_index(arr[j].index(down))]
        #print(down, up)
        if down == 6 or up == 6:
            if down == 5 or up == 5:
                sum_value += 4
            else:
                sum_value += 5
        else:
            sum_value += 6
    #print(sum_value)
    if sum_value > max_sum:
        max_sum = sum_value

print(max_sum)