# 연속된 문자 검사하기
message = "hello"
for index in range(1, len(message)): # 두번째 문자 기준
    if message[index-1] == message[index]:
        print("연속된 문자가 존재")
        break


    
