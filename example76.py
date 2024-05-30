# 학생 10명의 점수를 가지고 순위를 구함
# 상위 30%에 대한 평균
score = [87, 79, 88, 89, 94, 92, 82, 75, 95, 71]
# 상위 30% 인원수 구하기
high = int(len(score) * 0.3)
score.sort(reverse=True)
total = 0
for index in range(high):
    total += score[index]
answer = total / high
print(answer)
