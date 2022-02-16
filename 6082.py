a = input()
n = int(a)

for i in range(1, n+1):
    if i % 10 == 3:
        print("X", end=' ')  # 출력 후 공백문자(빈칸)으로 끝냄
        i += 1
    elif i % 10 == 6:
        print("X", end=' ')
        i += 1
    elif i % 10 == 9:
        print("X", end=' ')
        i += 1
    else:
        print(i, end=' ')
        i += 1
