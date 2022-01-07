import sys
input = sys.stdin.readline

N = list(input()[:-1])
L = len(N) - 1

for bitnum in range(2**L):
    t = N.copy()
    for i in range(L):
        if (bitnum>>i)&1:
            t[i] += '-'
        else:
            t[i] += '+'
    if 7 == eval(''.join(t)):
        print(''.join(t) + "=7")
        break
