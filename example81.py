# 문자열에서 연속하는 중복문자를 제거하기
message = "seeentttencccee"  # sentence
answer = message[0]
# 이전 문자와 현재 문자를 비교 (시작인덱스 1)
for index in range(1, len(message)):  # 1~15
    if message[index-1] != message[index]:
        answer += message[index]
print(answer)
        
    

