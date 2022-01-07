import sys

input = sys.stdin.readline

N = int(input())
T = [int(input())for _ in range(N)]

candidate = []

for bitnum in range(2**N):
    A = 0
    B = 0
    for i in range(N):
        if (bitnum>>i) & 1:
            A += T[i]
        else:
            B += T[i]
    candidate.append(max(A,B))
print(min(candidate))


