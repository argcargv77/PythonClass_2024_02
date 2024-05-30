# 사전 (dictionary)
# A는 B이다 : A와 B를 쌍으로 표현
# A는 key(키), B는 value(값)
# 키와 값의 쌍(key:value)을 나열
# 사전은 { } 중괄호로 묶어서 표현
# 사전은 비순차자료 -> 인덱스가 없음

person = {"id":1234, "name":"홍길동", "age":25}
print(person["id"])  # 키를 사용하여 값을 출력
print(person["age"])

a = {1:"one", 2:"two", 3:"three"}  # 키를 정수
print(a[2])  # "two"
b = {"one":1, "two":2, "three":3}  # 키가 문자열
print(b["three"])
c = {1:"one", "two":2, "three":"삼"}
print(c["three"])
d = {3.14:"pi", 1.2:"eye"}  # 키가 실수
print(d[3.14])
e = {"name":"kim", "score":[100, 90, 88], "test":(1, 2, 3)}
# 값이 리스트, 튜플
print(e["score"], e["test"])
# f = {[1,2,3]:"score"}  # 리스트(변경 가능)는 키가 될 수 없다
g = {(1,2,3):"score"}  # 튜플은 키로 가능
print(g[(1,2,3)])










