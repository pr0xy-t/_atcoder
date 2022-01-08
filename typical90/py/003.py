import queue
import sys
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N+1)] 
for i in range(N-1):
    Ai, Bi = map(int,input().split())
    G[Ai].append(Bi)
    G[Bi].append(Ai)

dist = [0] * (N+1)

# 頂点startから各頂点までの距離をBFSで求める
def bfs(start):
    for i in range(N+1):
        dist[i] = -1
    Q = queue.Queue()
    Q.put(start)
    dist[start] = 0
    while not Q.empty() :
        v = Q.get()
        for v2 in G[v]:
            if dist[v2] == -1:
                dist[v2] = dist[v] + 1
                Q.put(v2)





#print(G)
bfs(1)
v = dist.index(max(dist))
bfs(v)
print(max(dist)+1)
