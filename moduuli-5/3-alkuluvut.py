number = int(input("Anna numero: "))
prime = True

if number <= 1:
    prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False

if prime:
    print(f"{number} on alkuluku")
else:
    print(f"{number} ei ole alkuluku")
