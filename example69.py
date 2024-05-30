# 문자열에서 특정 문자(1개) 삭제하기
account = "123-2345-34-7"  # "1232345347"
answer = ""
for a in account:
    '''
    if a == '-':
        continue
    answer += a
    '''

    if a != '-':
        answer += a
        
print(answer)
