# 주어진단어 리스트에서 길이가 5이상인 단어를 이어 붙이기
# 문자열을 가진 리스트
words = ["my", "favorite", "color", "is", "violet"]
answer = ""  # 빈 문자열 초기화
for w in words:
    if len(w) >= 5:
        answer += w
print(answer)
    
