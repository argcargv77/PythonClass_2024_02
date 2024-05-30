# 비밀번호를 힌트
# 알파벳문자는 #으로 표시, 숫자문자 *로 표시
password = "hello1234"  # #####****
hint = ""
for p in password:
    if p.isdigit():
        hint += "*"
    elif p.isalpha():
        hint += "#"
    else:
        hint += p
print(hint)

        
        
