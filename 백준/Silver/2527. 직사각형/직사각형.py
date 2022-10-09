# 정답인 코드 
for _ in range(4):
    points = list(map(int, input().split()))
    x1, y1, p1, q1 = points[:4]
    x2, y2, p2, q2 = points[4:]

    # 점에서 만나는 경우
    if (p1 == x2 and y1 == q2) or (p2 == x1 and y1 == q2) or (p1 == x2 and q1 == y2) or (p2 == x1 and q1 == y2):
        print('c')
    # 안만나는 경우
    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
    # 선에서 만나는 경우
    elif (x2 == p1) or (x1 == p2) or (q1 == y2) or (q2 == y1):
        print('b')
    # 겹치는 경우
    else:
        print('a')