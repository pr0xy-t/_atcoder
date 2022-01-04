N,Y = [ int(i) for i in input().split() ]

flag = False

for i in range(N+1):
    for j in range(N+1-i):
        if 10000 * i + 5000 * j + 1000 * (N-(i+j)) == Y:
            print(i,j,N-(i+j))
            flag = True
            break
    else:
        continue
    break
if not flag:
    print("-1 -1 -1")
