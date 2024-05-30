# 문자열 검사하기
message = "hello"
print(message.isalpha())  # 순수하게 알파벳으로 구성?
message = "1234"
print(message.isdigit())  # 순수하게 숫자로 구성?
message = "hello1234"     # 순수하게 숫자문자로만 구성? (다른 문자는 안됨)
print(message.isalnum())
# islower(), isupper(), isspace()

nchr = 0
nnum = 0
noth = 0
message = input("문자열 입력 : ")
for m in message:
    if m.isalpha():
        nchr += 1
    elif m.isdigit():
        nnum += 1
    else:
        noth += 1
print(nchr, nnum, noth)




    







