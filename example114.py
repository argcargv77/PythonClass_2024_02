'''
파일 입출력
open() :  파일을 연다(접근) -> 파일에 대한 객체를 가져옴
'''

ans = []
kmu = open("kmu.txt", "r")	# 읽기 용도로 open
# kmu : 파일 객체

while True:
    data = kmu.readline()	# 파일의 한 줄을 읽는다
    # 파일을 끝까지 읽은 경우
    if not data:
        break
    ans.append(data)

print(ans)
kmu.close() 	# 파일을 닫음

# 기존의 파일 내용에 덮어쓰기 때문에 기존 내용은 사라짐
kmu = open("kmu.txt", "w")	# 쓰기 용도로 open
for index in range(1, 11):
    data = "%d line\n" %index
    kmu.write(data)
kmu.close()