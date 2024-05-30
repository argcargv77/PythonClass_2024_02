# 사전 메서드
number = {1:"one", 2:"two", 3:"three"}
# 사전에서 키만 뽑는 방법
print(number.keys())
print(number.values())
print(number.items())

for key in number.keys():
    print(key)

for value in number.values():
    print(value)
    
for k, v in number.items():
    print(k, v)
