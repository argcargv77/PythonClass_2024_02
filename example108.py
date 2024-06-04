'''
모듈(module): 함수의 집합
내장(함수)모듈 : 파이썬이 기본적으로 가지고 있는 함수들
특별한 모듈은 가져와서 사용해야 한다(import).
'''
import math
import calendar

number = 3.64
print(math.ceil(number))	# 소수올림수(소수자리가 존재하면 무조건 올림)
print(math.floor(number))	# 소수내림수(소수자리가 존재하면 무조건 내림)

calendar.prmonth(2024, 6)