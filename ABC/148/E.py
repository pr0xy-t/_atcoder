import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
if N % 2 == 0:
    # 10**18 > 5**25 , 10**18 < 5*26より
    for i in range(1,26):
        cnt += N // (2 * 5**i)
print(cnt)



