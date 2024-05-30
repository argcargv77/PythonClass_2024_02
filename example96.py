# 사전의 접근 : 사전[key] -> 값
number = {1:"one", 2:"two", 3:"three"}
# 항목 추가
number[4] = "four"
print(number)

# 사전도 반복이 가능
for n in number:
    print(n)  # 키가 출력

for n in number:
    print(number[n])  # 값을 출력

# 항목 삭제
del number[1]
print(number)


    
