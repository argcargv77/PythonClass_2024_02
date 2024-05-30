# 문자열에서 정수를 추출하여 총합 구하기
message = "korea 2021, 30day 6hour"
# 숫자 문자 1개를 하나의 숫자로 취급
# 2+0+2+1+3+0+6 = 14
answer = 0
for m in message:
    if m >= '0' and m <= '9':
        answer += int(m)
print(answer)

#---------------------------
# 숫자 문자가 연속으로 나올 경우 하나의 정수로 취급
# 2021+30+6 = 2057
message = "korea 2021, 30day 6hour"
answer = 0
number = 0  # 이전 초기값
for m in message:
    if m >= '0' and m <= '9':  # '0' <= m <= '9':
        # 숫자가 나오면 이전 값에 10을 곱해서 자리수를 올림
        number = number * 10 + int(m)
    else:
        # 숫자가 아닌 문자가 나오면
        answer += number
        number = 0  # 새로운 정수를 생성하기 위해 초기화
print(answer)
        









