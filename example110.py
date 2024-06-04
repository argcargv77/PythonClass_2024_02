import random

num1 = random.randint(1, 100)	# 임의의 정수

num2 = random.random()	# 임의의 실수

family = ["아빠", "엄마", "나", "동생"]
who = random.choice(family)
random.shuffle(family)	# 원본이 바뀜
print(family)