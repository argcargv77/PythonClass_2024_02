# 과일의 이름과 가격 정보를 사전으로 구성
fruit = {}  # 빈사전
for count in range(3):
    name = input("이름 : ")
    price = int(input("가격 : "))
    fruit[name] = price
print(fruit)
# {'apple': 1500, 'banana': 2000, 'lemon': 2500}
