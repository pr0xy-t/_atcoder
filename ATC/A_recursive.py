# A - 深さ優先探索
import sys
# [!] 再帰を使う時はsetrecursionlimitを変更しないと実行時エラーになる可能性がある
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

H, W = map(int,input().split())
# 迷路
cw = [ list(input()[:-1]) for _ in range(H)]
# 到達できる？
reached = [ [False] * W for _ in range(H)]

def search(x,y):
    # 迷路の外側か壁の場合は何もしない
#    print(x,y)
    if x<0 or H<=x or y<0 or W<=y or cw[x][y]=='#':
        return
    # 以前に到達していたら何もしない
    if reached[x][y]:
        return

    reached[x][y] = True # 到達したとチェック

    # ４方向を試す
    search(x-1,y)
    search(x+1,y)
    search(x,y-1)
    search(x,y+1)

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


#print(sx,sy)
#print(gx,gy)
#
#print(cw)
#print_2darr(cw,isbool=False)
#print("===before===")
#print_2darr(reached)

search(sx,sy)
#print("===after===")
#print_2darr(reached)

if reached[gx][gy]:
    print("Yes")
else:
    print("No")



