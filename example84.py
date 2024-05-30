# 문자열 메서드
message = "HeLLo"
print(message.upper()) # 대문자로 변환
print(message.lower()) # 소문자로 변환
print(message.swapcase())  # hEllO
print(message.capitalize())  # Hello

#---------------
message = "good morning good afternoon"
print(message.count("good"))  # 2
print(message.count("oo"))  # 3
print(message.count("o"))  # 7

#---------------
print(message.index("good"))  # 0 (처음 나오는 위치)
print(message.index("good", 5))  # 13
print(message.find("good"))  # 0 (처음 나오는 위치)
print(message.find("good", 5))
# 뒤에서 부터 검색
# rindex(), rfind()

#---------------
# 교체 (찾아서 바꿔라) : 원본은 그대로
answer = message.replace("good", "hi") # 별도의 오류는 없음
print(answer)

#---------------
message = "      hello      "
print(len(message))  # 17
# 앞 뒤의 공백을 제거 : strip()
# lstrip() : 왼쪽공백 제거, rstrip() : 오른쪽 공백 제거
print(message.strip())  # 기본 공백제거

message = "------hello------"
print(message.strip("-")) # 제거할 문자 지정
# tip
message = "   h   ell   o   "
message = message.replace(" ", "")
print(message)

message = "123-345-1-56"
message = message.replace("-", "")
print(message)




















