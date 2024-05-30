# 보수 문자 구하기
# 예) 3에 대한 7의 보수 : 4
# 주어진 문자열에서 숫자는 9의 보수로 바구어 출력
# "hi2015" -> "hi7984"
# 아스키 코드 활용
message = "hi2015"
answer = ""
for m in message:
    if m >= '0' and m <= '9':
        # m의 보수문자
        # 보수를 결정하는 문자 : 두 아스키 코드를 합
        # 9의 보수 : 'i'(105) -> '0'(48) + '9'(57)
        code = ord('i') - ord(m)
        m = chr(code)    
    answer += m
print(answer)
