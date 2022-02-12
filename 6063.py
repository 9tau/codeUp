a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a >= b) else b)
# (a>=b) : True 또는 False를 평가할 조건식
# a : 위의 평가가 True 일 때 사용할 값
# b : 위의 평가가 True가 아닐 때 사용할 값

print(int(c))
