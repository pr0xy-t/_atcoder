import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()

ans = 0
for i in range(len(A)):
    ans += abs(A[i]-B[i])

print(ans)
