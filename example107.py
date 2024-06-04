def getCounter(vote, person):
    counter = [0] * person
    for v in vote:
        counter[v-1] += 1
    return counter
    
def getName(counter, name):
    max = counter[0]
    answer = name[0]
    for index in range(1, len(counter)):
        if max < counter[index]:
            max = counter[index]
            answer = name[index]
    return answer
    
def getChart(counter, name):
    for index in range(len(counter)):
        print("%s : " %name[index], end="")
        for star in range(counter[index]):
            print("*", end="")
        print("\n")

vote = [1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3]
name = ["홍길동", "박지성", "김연아"]
counter = getCounter(vote, len(name))
getChart(counter, name)

print("당선자 : %s" %getName(counter, name))