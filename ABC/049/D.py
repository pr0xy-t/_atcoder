from collections import defaultdict
import sys
input = sys.stdin.readline

N,K,L = map(int,input().split())
pq = [list(map(int,input().split())) for _ in range(K)]
rs = [list(map(int,input().split())) for _ in range(L)]

parent_highway = [0]*N
parent_railway = [0]*N
rank_highway = [0]*N
rank_railway = [0]*N

def init():
    for i in range(N):
        parent_highway[i] = i
        parent_railway[i] = i

def find_root(parent_list,x):
    if parent_list[x] == x:
        return x
    else:
        parent_list[x] = find_root(parent_list,parent_list[x])
        return parent_list[x]

def is_same_group(parent_list,x,y):
    return find_root(parent_list,x) == find_root(parent_list,y)

def unite(parent_list,rank_list,x,y):
    x = find_root(parent_list,x)
    y = find_root(parent_list,y)
    if x == y:
        return
    if rank_list[x] < rank_list[y]:
        parent_list[x] = y
    else:
        parent_list[y] = x
        if rank_list[x] == rank_list[y]:
            rank_list[x] += 1


init()
for i in pq:
    unite(parent_highway,rank_highway,i[0]-1,i[1]-1)
parent_highway2 = [find_root(parent_highway,i) for i in range(N)]
for i in rs:
    unite(parent_railway,rank_railway,i[0]-1,i[1]-1)
parent_railway2 = [find_root(parent_railway,i) for i in range(N)]


cache = defaultdict(int)
for i in range(N):
    cache[(parent_highway2[i],parent_railway2[i])] += 1
print(*[cache[(parent_highway2[i],parent_railway2[i])] for i in range(N)])
    
#print(parent_highway)
#print(parent_railway)

