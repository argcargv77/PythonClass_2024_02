'''
객체지향언어
객체(object)
객체는 속성(data)과 메소드로 구성되어있다.
클래스(class) : 객체를 설계하기 위한 설계도

객체 지향 프로그래밍 -> 클래스를 설계하고 객체를 생성하여 프로그램을 작성한다.
객체는 클래스로부터 생성된 인스턴스다.(클래스의 인스턴스이다.)
'''

# 클래스
class Point:
    # 속성 (초기화 필수)
    x = 0
    y = 0
    
    # 생성자(constructor)
    # 객체가 만들어지는 순간에 딱 한번 자동으로 호출되는 메서드
    # __init__ 이름으로 정의한다
    def __init__(self, x=None, y=None):	# 파라미터 정의하는 과정에서 초깃값 설정 가능
        self.x = x
        self.y = y
        
    # 설정자(setter)
    # self : 자기 자신을 나타내는 객체, 클래스 내부의 속성과 메서드를 표현할 때 사용
    # 		반드시 메서드 첫번째 인수로 정의해야 함.
    def SetPoint(self, x, y):
        self.x = x
        self.y = y
	
    # 접근자(getter)
    def Getx(self):
        return self.x
            
    def Gety(self):
        return self.y
    
    # 메서드
    def message(self):
        print("Point 클래스")
        
    # 출력 메서드
    def displayPoint(self):
        print("(%d, %d)" %(self.Getx(), self.Gety()))    
        
# 클래스로부터 객체를 생성
pt1 = Point()
print(pt1.x, pt1.y)		# 0, 0
pt1.message()
pt1.SetPoint(100, 200)
print(pt1.x, pt1.y)		# 100, 200	이렇게 직접 접근 방식은 좋지 않음
print(pt1.Getx(), pt1.Gety())		# 메서드를 이용해 간접 접근하는 것이 좋다
pt1.displayPoint()

pt2 = Point()
pt2.SetPoint(300, 400)
pt2.displayPoint()

pt3 = Point()
pt3.SetPoint(500, 600)
pt3.displayPoint()

pt4 = Point(700, 800)
pt4.displayPoint()