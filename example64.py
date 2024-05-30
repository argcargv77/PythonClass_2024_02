# 문자열 : 문자의 나열
# 문자열 표현 : "A", 'A'
# 문자의 정체 : 문자는 문자라는 가면을 쓴 정수(코드값)

# 아스키(ASCII)코드
# '0'~'9' : 48~57
# 'A'~'Z' : 65~90
# 'a'~'z' : 97~122

print(ord('A'))  # 문자에 대한 코드 값
print(chr(65))   # 코드에 대한 문자

# 문자의 크기 비교
print('A' > 'B')  # False
print('a' > 'b')
print('A' > 'a')  # False
print("korea" > "japan")   # True

# 문자(문자열)의 연결 : + 연산자
# 문자열 합치기 : 합 구하는 방식
# 문자(문자열) 반복 : * 연산자

# 문자열 : 순차자료
# 인덱스를 사용하여 문자를 탐색
# 문자열의 길이 : len()
# 부분 문자열 : 슬라이싱 [2:7]

# 문자열의 문자변경은 안됨
message = "hello"
print(message[0])  # 'h'
# message[0] = 'k'  # 오류
# 문자의 변경은 리스트로 변환 후 변경하고 다시 문자열로 조립
message = list(message)  # ['h', 'e', 'l', 'l', 'o']
message[0] = 'k'
total = ""  # 초기값은 빈문자열
for m in message:
    total += m
print(total)

# 문자열의 포함여부 : in 연산자 (if문)
message = "hello"
print('k' in message)

# 문자열도 객체이다
# 문자열의 다양한 메서드도 존재











