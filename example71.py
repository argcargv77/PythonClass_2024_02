# 임의의 문자열을 입력받아 영문자 숫자 개수 구하기
# "hello#$%^1234"
nchar = 0  # 문자개수
nnumb = 0  # 숫자개수
nothr = 0  # 기타개수
message = input("문자열 입력 : ")
for m in message:
    if (m >= 'a' and m <= 'z') or (m >= 'A' and m <= 'Z'):
        # 영문자 판단
        nchar += 1
    elif m >= '0' and m <= '9':  # 숫자 판단 (48~57)
        nnumb += 1
    else:
        nothr += 1
        
print(nchar, nnumb, nothr)      

