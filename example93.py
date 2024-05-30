# 문자열 합치기
message = "hello" # -> "kello"
message = list(message)  # ['h', 'e', 'l', 'l', 'o']
message[0] = 'k'
'''
total = ""
for m in message:
    total += m
print(total)
'''
# 널문자를 구분기호
message = "".join(message)
print(message)


