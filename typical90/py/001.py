import sys
input = sys.stdin.readline

N, L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))
A.append(L)

ok = 1
ng = L

while (ng-ok)>1:
    mid = (ng+ok)//2
    # 全てが長さmid以上のK+1個のピースに分割可能か
    start = 0
    cnt = 0
    for i in range(N+1):
        if (A[i]-start)>=mid:
            cnt += 1  
            start = A[i]
    if cnt >= (K+1):
        ok = mid
    else:
        ng = mid
print(ok)




