n = int(input())
a = 0
for i in range(n+1):  # 0~c까지 출력
    if i % 2 == 0:
        a += i
print(a)
