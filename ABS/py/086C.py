import sys

input = sys.stdin.readline

N = int(input())

t,x,y = [0,0,0]

flag = True

for i in range(N):
    ti,xi,yi = [ int(j) for j in input().split() ]

    d = abs(xi - x) + abs(yi - y)
    dt = ti - t
    if dt >= d and (dt - d) % 2 == 0:
        t = ti
        x = xi
        y = yi
        continue
    else:
        flag = False
        break


if flag :
    print("Yes")
else:
    print("No")
