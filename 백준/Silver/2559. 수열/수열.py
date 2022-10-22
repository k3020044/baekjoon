import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().split()))

result = []
result.append(sum(num[:K]))

for i in range(N-K):
    result.append(result[i] - num[i] + num[i+K])

print(max(result))