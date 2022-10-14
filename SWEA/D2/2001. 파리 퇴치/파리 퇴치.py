def values(i, j):
   global max_value
   sum_value = 0
   for n in range(k):
       for m in range(k):
           sum_value += arr[i+n][j+m]
   if sum_value > max_value:
       max_value = sum_value

t = int(input())
for tc in range(1, t+1):
   n, k = map(int, input().split())
   arr = [list(map(int, input().split())) for _ in range(n)]

   max_value = 0
   for i in range(n-k+1):
       for j in range(n-k+1):
           #print(i, j)
           values(i, j)

   print(f'#{tc} {max_value}')
