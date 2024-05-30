# 문자열로 구성된 점수를 입력받아 합 구하기
score = input("점수 입력 : ")  # "100- 90-89 -75"
total = 0
for s in score.split('-'):  # ["100", "90", "89", "75"]
    total += int(s.strip())
print(total)
