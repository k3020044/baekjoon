import sys
input = sys.stdin.readline

N , M = map(int,input().rstrip().split())

Z = (M *100)//N
ans = 0
# start , end + 예외  선언해주기
if Z >= 99:
    print(-1)
else:
    ans = 0
    start =1
    end = 1000000000
# 승률 계산해주기 !!  // vs int( a / b) 의 차이점 파악해두기(부동소수점 오류)
    while start <= end:
        mid = (start+end)//2
        if (M+mid)*100 // (N+mid) > Z:
            ans = mid
            end = mid -1
        else:
            start = mid+1
    print(ans)