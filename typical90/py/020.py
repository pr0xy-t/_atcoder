import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())

if pow(c,b)>a:
    print("Yes")
else:
    print("No")
