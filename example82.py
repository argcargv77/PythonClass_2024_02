# 펠린드롬(palindrom)
# 앞에서 읽으나 뒤에서 읽어도 같은 문장
# racecar, noon
# "never odd or even." -> "neveroddoreven"
message = "never odd or even."
answer = True
# 공백 "." 제거
rmessage = ""
for m in message:
    if m != " " and m != ".":
        rmessage += m
print(rmessage)

for index in range(len(rmessage)):
    if rmessage[index] != rmessage[len(rmessage)-1-index]:
        answer = False
        break
print(answer)

