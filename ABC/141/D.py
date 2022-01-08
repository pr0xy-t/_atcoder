import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(lambda x: -1*int(x),input().split()))
heapq.heapify(A)
for _ in [0]*M:
    item = -1 * heapq.heappop(A)
    A.append(-1*(item//2))

A = list(map(lambda x: -1*x, A))
print(sum(A))

