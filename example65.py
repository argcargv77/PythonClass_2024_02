# 문자열에서 공백의 개수 구하기
message = "welcome to korea"
answer = 0
for m in message:
    if m == " ":
        answer += 1
print(answer)

# 문자열에서 단어 찾기
message = "welcome to korea"
word = "to"
if word in message:
    print("있다")
else:
    print("없다")




    
