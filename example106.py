# 파이썬에서는 여러 개의 반환값이 가능
def add(a, b):
			return a+b

def sub(a, b):
			return a-b

def calculator(a, b):
			add = a + b
			sub = a - b
			return add, sub			# 여러 개의 값을 반환할 경우 튜플로 생성하여 반환함.

print(“합 : “, add(10, 20))
print(“차 : ”, sub(10, 20))
print("결과 : ", calculator(10, 20))