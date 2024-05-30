# ISBN 문제 : 국제적으로 도서에 붙이는 고유한 식별자
# ISBN 판별
# "978-89-7050-555-8"
# 13자리 중 마지막 숫자 체크값
# 가중치 (12자리) : "131313131313"
# 검사 : ISBN의 갑 자리값과 가중치를 곱의 합을 구하고
# 합을 10으로 나눈 나머지를 구해서 다시 10에서 나머지를 뺌
# 나온 수를 체크값과 비교
isbn = "9788970505558"
weight = "131313131313"
answer = False
total = 0
for index in range(len(isbn)-1):
    total += int(isbn[index]) * int(weight[index])
    
check = 10 - (total % 10)
if check == 10:  # 나머지가 0일 경우
    check = 0

if check == int(isbn[12]):
    answer = True
print(answer)







