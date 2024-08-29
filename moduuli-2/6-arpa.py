import random

code1 = ""
code2 = ""

for _ in range(3):
    code1 += str(random.randint(0,9))

for _ in range(4):
    code2 += str(random.randint(1,6))

print(code1)
print(code2)
