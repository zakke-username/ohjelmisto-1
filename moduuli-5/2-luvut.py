numbers = []

number_str = input("Syötä numero: ")
while number_str != "":
    numbers.append(float(number_str))
    number_str = input("Syötä numero: ")

numbers.sort(reverse=True)
for n in numbers[:5]:
    print(n)
