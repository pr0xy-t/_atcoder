import sys
import queue
input = sys.stdin.readline

R, C = map(int,input().split())
sy, sx = map(int,input().split())
sy, sx = sy-1, sx-1
gy, gx = map(int,input().split())
gy, gx = gy-1, gx-1
c = [ list(input()[:-1]) for _ in range(R)]

reached = [[-1]*C for _ in range(R)]
q = queue.Queue()


def bfs(s_y, s_x, g_y, g_x):
    y, x = s_y, s_x
    reached[y][x] = 0
    q.put((y, x))

    while not (y==g_y and x==g_x):
        y, x = q.get()

        for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
            if y+i<0 or R<=y+i or x+j<0 or C<=x+j:
                continue
            if c[y+i][x+j] != '#' and reached[y+i][x+j] == -1:
                reached[y+i][x+j] = reached[y][x] + 1
                q.put((y+i, x+j))
    
    return reached[g_y][g_x]

print(bfs(sy, sx, gy, gx))





