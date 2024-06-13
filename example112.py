class Area:
    # 속성
    width = 0
    height = 0

    #생성자
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    #초기값 설정 : setter
    def setData(self, width, height):
        self.width = width
        self.height = height

    # 메서드
    def computeSquare(self):
        return self.width*self.height
    
    def computeTriangle(self):
        return self.width*self.height/2
    
# 객체를 생성
my1 = Area()
my1.setData(100, 200)
print("삼각형 면적 : ", my1.computeTriangle())
print("사각형 면적 : ", my1.computeSquare())

my2 = Area()
print("삼각형 면적 : ", my2.computeTriangle())
print("사각형 면적 : ", my2.computeSquare())

my2 = Area(100)
print("삼각형 면적 : ", my2.computeTriangle())
print("사각형 면적 : ", my2.computeSquare())

my2 = Area(100,200)
print("삼각형 면적 : ", my2.computeTriangle())
print("사각형 면적 : ", my2.computeSquare())