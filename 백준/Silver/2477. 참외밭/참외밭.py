n = int(input()) # 1m당 참외 개수

# 초기 좌표 (길이 최대가 500이기 때문에 -500 하더라도 양수이도록)
x = 500
y = 500
# 꼭짓점 6개 좌표 리스트에 넣기
lst = []
for _ in range(6):
	direction, length = map(int, input().split())
	# 북쪽
	if direction == 4:
		x -= length
		y = y
		lst.append((x, y))
	# 서쪽
	elif direction == 2:
		x = x
		y -= length
		lst.append((x, y))
	# 남쪽
	elif direction == 3:
		x += length
		y = y
		lst.append((x, y))
	# 동쪽
	else:
		x = x
		y += length
		lst.append((x, y))
#print(lst)
# y값 기준으로 오름차순 정렬하기, x[0]은 정렬안됨!!!!
lst.sort(key=lambda x:x[1])
#print(lst)
rectangle = 0
# 첫번째 사각형 = 1,2 x값 차이 * 1,3 y값 차이
# 두번째 사각형 = 3,4 y값 차이* 4,5 x값 차이
rectangle = abs(lst[1][0] - lst[0][0]) * abs(lst[2][1] - lst[0][1]) + abs(lst[4][1] - lst[3][1]) * abs(lst[5][0] - lst[4][0])
print(n * rectangle)