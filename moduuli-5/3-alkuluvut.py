n = int(input("Anna numero: "))

prime = True
if n <= 1:
    prime = False
else:
    for i in range(2, n//2+1):
        if n % i == 0:
            prime = False

if prime:
    print(f"{n} on alkuluku")
else:
    print(f"{n} ei ole alkuluku")
