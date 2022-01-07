import sys
input = sys.stdin.readline

N,M = map(int,input().split())
X,Y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


# t時以降で最も出発が早い飛行機の時刻を探索する
def binary_search(data,time):
    ng = -1
    ok = len(data)
    while ok-ng > 1:
        mid = (ng+ok)//2
        if data[mid]>=time:
            ok = mid
        else:
            ng = mid

    return ok

a_arrival_time = 0
cnt = 0

while True:
    a_departure_time = a[binary_search(a,a_arrival_time)]
    b_arrival_time = a_departure_time + X

    if b_arrival_time > b[-1]:
        break

    b_departure_time = b[binary_search(b,b_arrival_time)]
    a_arrival_time = b_departure_time + Y

    cnt += 1

    if a_arrival_time > a[-1]:
        break

print(cnt)




