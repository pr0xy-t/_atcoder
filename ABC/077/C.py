import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

# Aの中でサイズs未満で最大サイズのパーツを探索
def binary_search_for_A(s):
    ok = -1
    ng = len(A)
    while ng - ok > 1:
        mid = (ng+ok)//2
        if A[mid]<s:
            ok = mid
        else:
            ng = mid
    return ok

# Cの中でサイズsより大きいもので最小のサイズのパーツを探索
def binary_search_for_C(s):
    ok = len(C)
    ng = -1
    while ok - ng > 1:
        mid = (ng+ok)//2
        if C[mid]>s:
            ok = mid
        else:
            ng = mid
    return ok

ans = 0

for b in B:
    ans += (binary_search_for_A(b)+1) * (len(C)-binary_search_for_C(b))

print(ans)



