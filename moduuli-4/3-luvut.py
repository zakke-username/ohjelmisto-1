numbers = []
number = input("Anna numero: ")

while number != "":
    numbers.append(float(number))
    number = input("Anna numero: ")

print(f"Pienin: {min(numbers)}, suurin: {max(numbers)}")