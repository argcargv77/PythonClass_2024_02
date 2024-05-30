# 문자열에서 문자, 숫자 개수 구하기
letter = {"문자":0, "숫자":0, "기타":0}
message = "hello1234!@#$%^"
for m in message:
    if m.isalpha():
        letter["문자"] += 1
    elif m.isdigit():
        letter["숫자"] += 1
    else:
        letter["기타"] += 1
        
print(letter)
for l in letter:
    print("%s : %d개" %(l, letter[l]))




