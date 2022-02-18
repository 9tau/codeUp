a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)
c = 0
for i in range(1, n+1):
    m = (a + (i-1)*d)

print(m)
