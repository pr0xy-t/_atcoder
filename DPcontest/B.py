import sys
input = sys.stdin.readline

N, K = map(int,input().split())
h = list(map(int,input().split()))

dp = [ 10**9 + 1 ] * N

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2,N):
    
    for j in range(1,K+1):
        dp[i] = min(dp[i], dp[i-j] + abs(h[i]-h[i-j])) 

print(dp[-1])

