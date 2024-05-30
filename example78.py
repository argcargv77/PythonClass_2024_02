# 문자열과 인덱스
# 문자열은 인덱스로 접근 가능
# 인덱스가 음수인것은 파이썬만 가능
message = "welcome!"
print(message[0], message[1])  # w e
print(message[-1], message[len(message)-1])  # 마지막 문자

# 문자열에서 문자 변경은 안됨
# message[0] = 'k'  # 오류
# 문자열을 리스트로 변환한 후 리스트에서 문자를 변경
# 리스트의 문자를 합쳐나감
message = list(message)
# ['w', 'e', 'l', 'c', 'o', 'm', 'e', '!']
message[0] = 'k'
total = ""
for m in message:
    total += m
print(total)  # kelcome!

# 문자열 탐색
message = "welcome"
index = 0
while index < len(message):  # 0~6
    print(message[index])
    index += 1

for index in range(len(message)):
    print(message[index])

    






