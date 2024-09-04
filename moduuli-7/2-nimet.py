import random

names = []

while True:
    name = input("Anna nimi: ")
    if name == "":
        break
    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.append(name)

random.shuffle(names)
for i in names:
    print(i)
