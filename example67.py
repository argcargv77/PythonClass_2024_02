# 문자열 처리 시간 구하기
# 문자 4개당 1분 걸림
message = ["hello", "welcome", "fighting!", "hi"]
answer = 0
for m in message:
    answer += len(m) // 4
    if len(m) % 4 > 0:  # 나머지가 존재하면
        answer += 1
print(answer)
