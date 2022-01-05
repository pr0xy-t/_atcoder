import sys

input = sys.stdin.readline

N,K = map(int,input().split())
A = list(map(int,input().split()))

ok = -1
ng = len(A)

def is_ok(i):
    return A[i] < K

while (ng - ok) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

if ng == len(A):
    print("-1")
else:
    print(ng)
