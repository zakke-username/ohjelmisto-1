names = set()

while True:
    name = input("Anna nimi: ")
    if name == "":
        break
    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(name)

for i in names:
    print(i)
