# 회원 등급에 따른 할인금액 구하기
# S:5%, G:10%, V:15%
sale = {"S":0.95, "G":0.9, "V":0.85}
grade = input("등급 : ")
price = int(input("금액 : "))

for key in sale:
    if grade == key:
        pay = price * sale[key]

print(pay)
