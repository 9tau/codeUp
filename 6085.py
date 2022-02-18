w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)

n = (w*h*b) / (8 * 1024 * 1024)

m = round(n, 2)

print(m, 'MB')
