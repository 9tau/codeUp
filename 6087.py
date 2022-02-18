n = int(input())

for i in range(n+1):
    if i % 3 == 0:
        continue     # 다음 반복 단계로 넘어간다.
    print(i, end=' ')
