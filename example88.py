# 문자와 숫자를 반드시 섞어서 사용
password = input("비밀번호 : ")
if password.isalpha() or password.isdigit():
    print("문자와 숫자를 섞어야 함")
else:
    print("정상")
