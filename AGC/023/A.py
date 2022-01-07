# 累積和
import sys
import collections
input = sys.stdin.readline

N = int(input())
A = list( map(int,input().split()))
S = [0]*(N+1)

for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]

ans = 0
s2 = collections.Counter(S)
for i in s2:
    t = s2.get(i)
    # tC2
    ans += (t*(t-1))//2

print(ans)



