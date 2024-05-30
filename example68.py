# 5개의 단어를 입력 받아 합치기
message = ""
for count in range(5):
    word = input("단어 입력 : ")
    message += word
    # 다음 단어가 있으면 , 삽입
    if count != 4:
        message += ' '
print(message)
