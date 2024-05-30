# split() 메서드 : 문자열 분리
# 주어지는 데이터는 문자열에 구분문자로 구분되어짐
# 구분문자를 가지고 요소로 구분하야 리스트로 생성
message = "hello world korea"  # 공백을 구분 문자
# ["hello", "world", "korea"]
message = message.split()
print(message)

message = "hello,korea,world"
message = message.split(',')
print(message)






