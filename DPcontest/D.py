import sys
input = sys.stdin.readline

N, W = map(int,input().split())
wv = [ list(map(int,input().split())) for _ in range(N) ]

dp = [ [0 for j in range(W+1)] for i in range(N)]
for i in range(wv[0][0], W+1):
    dp[0][i] = wv[0][1]


for i in range(1,N):
    for j in range(W+1):
        if j >= 1:
            if j-wv[i][0] >= 0:
                dp[i][j] = max( dp[i-1][j], dp[i-1][j-wv[i][0]] + wv[i][1] , dp[i][j-1] )
            else:
                dp[i][j] = max( dp[i-1][j],  dp[i][j-1] )
        else:
            if j-wv[i][0] >= 0:
                dp[i][j] = max( dp[i-1][j], dp[i-1][j-wv[i][0]] + wv[i][1] )
            else:
                dp[i][j] = dp[i-1][j] 


print(dp[-1][-1])
