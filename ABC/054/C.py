# 順列(n!)の全探索
# n > 10 だと厳しそう
import sys
import itertools
input = sys.stdin.readline

N, M = map(int,input().split())
ab = [ set(list(map(int,input().split()))) for _ in range(M)]
#print(ab)
permutation_list = [ [1]+list(i) for i in list(itertools.permutations(range(2,N+1))) ]
#print(permutation_list)

cnt = 0

for i in permutation_list:
    flag = True
    for j in range(N-1):
        if not set( i[j:j+2]) in ab:
            flag = False
            break
    if flag:
        cnt += 1


print(cnt)


