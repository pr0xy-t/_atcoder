import sys
input = sys.stdin.readline

S = [0] * 10**5

prime_list = [True] * 10**5

def gen_prime_list(n):
    prime_list[0], prime_list[1] = False, False

    for i in range(2,int(pow(n,0.5))):
        if not prime_list[i]:
            continue
        for j in range(i*i,n,i):
            prime_list[j] = False
    return prime_list






def judge(n):
    if prime_list[n] and prime_list[(n+1)//2]:
        return 1
    else:
        return 0

gen_prime_list(10**5)

for i in range(1,10**5):
    S[i] = S[i-1] + judge(i)


Q = int(input())
lr = [ list(map(int,input().split())) for _ in range(Q)]
for i in lr:
    print(S[i[1]] - S[i[0]-1])
