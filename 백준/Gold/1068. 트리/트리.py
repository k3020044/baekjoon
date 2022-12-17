import sys
sys.setrecursionlimit(10 ** 6)


# dfs 탐색
def dfs(delete):
    # 제거할 노드를 -2로 정의
    tree[delete] = -2

    # 반복문을 통해 제거할 노드의 리프노드를 확인
    for i in range(n):
        if delete == tree[i]:
            # 제거할 리프 노드의 리프 노드를 재귀적으로 탐색
            dfs(i)


n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())
cnt = 0

# 노드를 삭제
dfs(d)

# 반복문을 통해 제거할 노드가 아니고 트리에 해당 노드의 리프 노드가 없다면 카운트
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)
