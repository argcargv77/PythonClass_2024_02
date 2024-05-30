# 매개변수와 인수의 네이밍은 동일해도 무관하다
# 매개변수는 지역변수이기 때문
def sample(d):
   b = 20
    c = 30
    print(a)   # a는 전역변수
    print(c)   # 지역이 우선이기 때문에 30이 출력된다.
    print(d)   # 50이 출력된다, 전역변수 d와 지역변수 d는 서로 다른 객체이다.
    
a = 10    
c = 40
d = 50
sample(d)   
# 호출 시에 a의 값이 출력된다, 전역변수와 지역변수를 동일한 네이밍 할 시에 지역을 우선(c=30 출력)
print(b)   # 출력 시 오류 발생, b는 sample() 내부의 지역변수이기 때문


def getLarge(num1, num2):
    if num1 > num2:
        max = num1
    else:
        max = num2
    return max
        
def getMax(num1, num2, num3):
    if num1 > num2:
        max = num1
    else:
        max = num2
    if max < num3:
        max = num3
    return max

def getMaxData(numlist):
    max = numlist[0]
    for n in numlist:
        if max < n:
            max = n
    return max
    
def getMaxItem(*num):   # * : 가변인수, 인수들을 튜플로 처리한다.
    total = 0
    for n in num:
        total += n
    return total

number1 = 10
number2 = 20
number3 = 30
maxnum1 = getLarge(number1, number2)
print(maxnum)

maxnum2 = getMax(number1, number2, number3)
print(maxnum2)

number = [10, 20, 1000, 40, 50]
print(getMaxData(number))

getMaxItem(10, 20, 30, 40, 50)
