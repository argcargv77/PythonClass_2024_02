# 비밀번호 조건 체크하기
# 한개 이상의 대문자 포함
# 두개 이상의 소문자를 포함
# 두개 이상의 숫자를 포함
# 한개이상의 특수문자 포함
# 길이는 12자이상

password = input("비밀번호 설정 : ")
check = [0] * 4  # [소문자, 대문자, 숫자, 특수]
sletter = "~!@#$%^&*"
if len(password) >= 12:
    for p in password:
        if p >= 'a' and p <= 'z':
            check[0] += 1
        elif p >= 'A' and p <= 'Z':
            check[1] += 1
        elif p >= '0' and p <= '9':
            check[2] += 1
        elif p in sletter:
            check[3] += 1
    if check[0] >= 2 and check[1] >= 1 and check[2] >= 2 and check[3] >= 1:
        print("가능")
    else:
        print("불가능")
else:
    print("길이가 12자이상이어야 함")
        





