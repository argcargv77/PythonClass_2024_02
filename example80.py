# 문자열 거꾸로 표현하기
# "hello" -> "olleh"
message = "hello"
answer = ""
for index in range(len(message)):
    # index는 0부터 시작 -> 마지막 인덱스부터 접근하는 방법
    answer += message[len(message)-1-index]
print(answer)

#--------------------
answer = ""
for index in range(1, len(message)+1):
    answer += message[index * -1]
print(answer)

#--------------------
answer = ""
for index in range(len(message)-1, -1, -1):
    answer += message[index]
print(answer)

# -------------------
answer = ""
for index in range(-1, (-1)*len(message)-1, -1):
    answer += message[index]
print(answer)






    
    
