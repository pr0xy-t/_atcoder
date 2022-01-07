# 順列(n!)の全探索
import sys
import itertools
import math
input = sys.stdin.readline

N = int(input())
xy = [ list(map(int,input().split())) for _ in range(N)]

permutation_list = list(itertools.permutations(range(N)))

cnt = 0

for i in permutation_list:
    i2 = list(i)
    for j in range(N-1):
        cnt += math.sqrt(pow(xy[i2[j+1]][1]-xy[i2[j]][1],2) + pow(xy[i2[j+1]][0]-xy[i2[j]][0],2))
    

print(cnt/len(permutation_list))
