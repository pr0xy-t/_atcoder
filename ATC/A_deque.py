# A - 深さ優先探索
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int,input().split())
# 迷路
cw = [ list(input()[:-1]) for _ in range(H)]

def print_2darr(arr,isbool=True):
    for i in range(len(arr)):
        print(list(map(int,arr[i])) if isbool else list(arr[i]))

sx,sy = 0,0
gx,gy = 0,0
for h in range(H):
    for w in range(W):
        if cw[h][w] == 's':
            sx,sy = h,w
        elif cw[h][w] == 'g':
            gx,gy = h,w

stack = deque([[sx,sy]])
# 到達できる？
reached = [ [False] * W for _ in range(H)]
reached[sx][sy] = True

def dfs():
    while len(stack) > 0:
        h, w = stack.pop()
        if cw[h][w] == 'g':
            return True
        for i,j in ([1,0],[-1,0],[0,1],[0,-1]):
            h2, w2 = h+i,w+j
            if h2 < 0 or h2 >= H or w2 < 0 or w2 >= W:
                continue
            if cw[h2][w2] != '#' and reached[h2][w2] == False:
                reached[h2][w2] = True
                stack.append([h2,w2])

    return False

#print(sx,sy)
#print(gx,gy)
#
#print(cw)
#print_2darr(cw,isbool=False)
#print("===before===")
#print_2darr(reached)

#print("===after===")
#print_2darr(reached)

if dfs():
    print("Yes")
else:
    print("No")



