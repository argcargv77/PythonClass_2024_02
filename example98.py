# 사전 정보를 요소로 하는 리스트
student = []
for index in range(2):  # 리스트를 구성
    # 사전을 정의
    info = {}
    info["이름"] = input("이름 : ")
    info["나이"] = int(input("나이 : "))
    info["점수"] = int(input("점수 : "))
    student.append(info)

print(student)
# [{'이름': 'aaa', '나이': 12, '점수': 65},
#  {'이름': 'bbb', '나이': 43, '점수': 98}]
