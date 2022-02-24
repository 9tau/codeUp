n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)  # list d값에 0 추가

for i in range(n):
    d[a[i]] += 1  # a값 번호 리딩할 때마다 d 리스트에 추가

for i in range(1, 24):
    print(d[i], end='')  # 카운트된 값 출력
