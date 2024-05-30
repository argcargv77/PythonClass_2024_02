# 햄버거 총 열량 구하기
recipe = ["빵", "패티", "토마토", "양상추", "케첩", "마요네즈", "치즈", "양파"]
calroie = [168, 250, 20, 11, 15, 57, 60, 40]

numbers = input("햄버거 재료를 번호로 입력 : ")
# 1,2,4,7
total = 0
for n in numbers.split(","):
    index = int(n)-1
    total += calroie[index]
print(total)
