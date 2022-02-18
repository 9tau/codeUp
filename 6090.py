from re import X


a, m, n = input().split()

a = int(a)
m = int(m)
n = int(n)
x = 0

for i in range(1, n+1):
    z = (a*(m)**(i-1) + x)
    x = z
    print(x)
