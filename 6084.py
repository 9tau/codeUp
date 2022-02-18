h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

n = (h*b*c*s) / (8 * 1024 * 1024)

m = round(n, 1)

print(m, 'MB')
