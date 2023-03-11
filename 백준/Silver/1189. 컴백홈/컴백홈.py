import sys

input = sys.stdin.readline


# r: 행, c: 열, k: 거리
r, c, k = map(int, input().strip().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))

# 상, 우, 하, 좌
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 처음 한수의 위치를 1로 설정
graph[r - 1][0] = 1

# 가짓수를 세기 위한 변수
result = 0
# 집은 오른쪽 맨 위임
def dfs(row, col):
    global result
    # 한수가 집에 도달했을 경우
    if row == 0 and col == c - 1:
    	# k와 한수가 이동한 거리가 동일하다면 가짓수에 넣어줍니다.
        if graph[row][col] == k:
            result += 1
            return
        else:
            return
    for i in move:
        nrow = row + i[0]
        ncol = col + i[1]
        if nrow >= 0 and ncol >= 0 and nrow < r and ncol < c:
            if graph[nrow][ncol] == '.':
                graph[nrow][ncol] = graph[row][col] + 1
                dfs(nrow, ncol)
                # 다음의 케이스에서 이용하기 위해서 방문처리를 해제해줍니다.
                graph[nrow][ncol] = '.'


dfs(r - 1, 0)
print(result)