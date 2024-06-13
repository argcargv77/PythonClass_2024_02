'''
예외처리 : 오류처리
코드가 실행하는 도중에 예기치 않은 오류가 발생
오류가 발생할 지점을 예상해서 지정 : try
발생할 오류에 대한 종류를 가지고 처리 코드를 작성 : except
'''

num = 10
score = [10, 20, 30]


try:
    n = int(input("수 입력 : "))
	ans = num / n
    print(ans)
    
    print(score[3])
	    
except ZeroDivisionError as error:
    print(error)

except ValueError as error:
    print(error)
    
except IndexError as error:
    print(error)