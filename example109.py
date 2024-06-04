import example107

vote = [1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 3, 3, 3, 3, 3, 3]
name = ["홍길동", "박지성", "김연아"]
counter = example107.getCounter(vote, len(name))
example107.getChart(counter, name)
print("당선자 : %s" %example107.getName(counter, name))