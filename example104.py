'''
내장함수 : 파이썬이 가진 기본적인 함수들(input, range, print, len ...)

사용자함수 : 사용자가 직접 정의하는 함수
	함수를 만드는 이유는 재활용하기 위해서.
	def 키워드를 사용하여 생성.
    함수는 호출하기 전에 미리 정의되어야 함.
    
인수 : 함수로 전달하는 실제 데이터
매개변수 : 함수로 전달받는 데이터
->매개변수는 인수를 받아서 전달하는 변수

반환값 : 함수에서 만들어져 전달하는 데이터
'''

def getMessage1():
    print("hello")

def getMessage2(msg):
    print("hello" + msg)
            
def getMessage3(msg):
    result = "hello" + msg
    return result

getMessage1()

getMessage2("korea")

answer = getMessage3("korea")
print(answer)