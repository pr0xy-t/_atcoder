import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
X, Y = X-1, Y-1

ans = [0] * N

def min_distance(s,t):
    #print(s,t)
    if s > t:
        s, t = t, s
    return min(t-s,abs(X-s)+abs(Y-t)+1)

def bfs(n):
    for i in range(N):
        if i == n:
            continue
        ans[min_distance(n,i)] += 1


# 頂点ごとに他の頂点までの距離を求める
for i in range(N):
    bfs(i)

for i in  ans[1:] :
    print(i//2)
