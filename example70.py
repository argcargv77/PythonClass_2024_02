# 문자열에서 여러개의 문자 제거
message = "hello!@#1234&^%$"
# 제거할 문자들을 모아서 구성
letters = "~!@#$%^&*()_+"
answer = ""
for m in message:
    if m not in letters:
        answer += m
print(answer)
        
