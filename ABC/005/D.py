import sys
input = sys.stdin.readline

N = int(input())
D = [ list(map(int,input().split())) for _ in range(N)]
Q = int(input())
P = [int(input()) for _ in range(Q)]

# NxNの2次元累積和
# S[i][j] := 左上を(0,0)とした時(0,0),(i,0),(0,j),(i,j)が成す長方形の美味しさ値
S = [[0]*(N+1) for _ in range(N+1)]
for h in range(1,N+1):
    for w in range(1,N+1):
        S[h][w] = D[h-1][w-1] + S[h][w-1] + S[h-1][w] - S[h-1][w-1]


# 面積ごとの美味しさ値の最大値
oisisa_max_list = [0 for _ in range(N*N+1)]
for x1 in range(N):
    for x2 in range(x1+1, N+1):
        for y1 in range(N):
            for y2 in range(y1+1, N+1):
                area = (x2-x1)*(y2-y1)
                oisisa_max_list[area] = max(oisisa_max_list[area], S[x2][y2]-S[x1][y2]-S[x2][y1]+S[x1][y1])

for i in P:
    print(max(oisisa_max_list[:i+1]))
