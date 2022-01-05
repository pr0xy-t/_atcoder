import sys
input = sys.stdin.readline

N, W = map(int,input().split())
wv = [ list(map(int,input().split())) for _ in range(N) ]
v_max = 10**5+1

dp = [ [10**10 for j in range(v_max)] for i in range(N)]
dp[0][wv[0][1]] = wv[0][0]
dp[0][0] = 0

for i in range(1,N):
    for j in range(v_max):
        if j-wv[i][1] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-wv[i][1]]+wv[i][0])
        else:
            dp[i][j] = dp[i-1][j]


for i,j in enumerate(dp[-1][::-1]):
    if j <= W:
        print(v_max - 1 - i)
        break
