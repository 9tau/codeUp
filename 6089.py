a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)
c = 0
for i in range(1, n+1):
    m = (a*r ** (i-1))  # **은 제곱을 뜻한다

print(m)
