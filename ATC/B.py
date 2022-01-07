# B - Union Find
# 連結判定の問題
import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
PAB = [ list(map(int,input().split())) for _ in range(Q)]
parent = [0]*N

def init():
    for i in range(N):
        parent[i] = i

def find_root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x]) # 経路圧縮
        return parent[x]

def is_same_group(x,y):
    return find_root(x) == find_root(y)

def unite(x,y):
    x = find_root(x)
    y = find_root(y)
    if x == y:
        return
    parent[x] = y

#print(PAB)

init()
for i in PAB:
    if i[0] == 0: # 連結クエリ
        unite(i[1],i[2])
    else: # 判定クエリ
        if is_same_group(i[1],i[2]):
            print("Yes")
        else:
            print("No")


