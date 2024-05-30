# 문자열 합치기 : join() 메서드
a = "hello"  # 구분문자 역활
b = "1234"
c = a.join(b)  # a, b는 그대로
# a를 b에 삽입
d = b.join(a)
# b를 a에 삽입
print(c)  # 1hello2hello3hello4
print(d)

a = ":"
# b = [10, 20, 30, 40, 50]  # 오류
b = ["10", "20", "30", "40", "50"]  # "10:20:30:40:50"
# b는 리스트라도 가능하지만 단 요소가 문자열이어야 함
print(a.join(b))

a = '\n'  # 줄바꿈
b = ["hello", "world", "korea"]
print(a.join(b))







