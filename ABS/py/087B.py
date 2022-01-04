A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0

for i in range(A+1):
    for j in range(B+1):
        t = X - (500*i + 100*j)
        if 0 <= t <= 50*C:
            cnt += 1
print(cnt)

            
