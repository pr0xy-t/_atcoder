import sys
input = sys.stdin.readline

S = list(input()[:-1])

L = len(S) - 1

ans = 0

for bitnum in range(2**L):
    t = S.copy()
    for i in range(L):
        if (bitnum>>i) & 1:
            t[i] += "+"
    ans += eval(''.join(t))

print(ans)


