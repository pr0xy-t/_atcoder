import sys
input = sys.stdin.readline

N, M = map(int,input().split())
PY = [tuple(map(int,input().split())) for _ in range(M)]
#PY.sort(key = lambda x: x[1])
PY2 = sorted(PY,key=lambda x: x[1])

# 発行済番号リスト
counter = [0] * (N+1)
ans = {}

for i in PY2:
    p = i[0]
    number = counter[p] + 1
    counter[p] = number
    ans[i[1]] = number



for i in PY:
    print(str(i[0]).zfill(6) + str(ans[i[1]]).zfill(6))
