import sys

input = sys.stdin.readline

N = int(input())
AB =  [ list(map(int,input().split())) for i in range(N) ] 
AB.sort(key=lambda x: x[1])

Max = 0
Cnt = 0

for i,j in AB:
    if Max < i:
        Max = j
        Cnt += 1
print(Cnt)



