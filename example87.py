# 입력 데이터 검사

while True:
    name = input("이름 : ")
    if not name.isalpha():
        print("문자만 가능")
        continue
    
    age = input("나이 : ")
    if not age.isdigit():
        print("숫자만 가능")
        continue
    else:
        age = int(age)
        break

        
    
