# 문자 개수2
message = "hello1234!@#$%"
alpha = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
answer = [0, 0, 0]
for m in message:
    if m in alpha:
        answer[0] += 1
    elif m in number:
        answer[1] += 1
    else:
        answer[2] += 1       
print(answer)
