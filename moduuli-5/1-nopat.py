import random

dice = int(input("Kuinka monta noppaa heitetään? "))
total = 0
for i in range(dice):
    total += random.randint(1,6)

print(f"Tulos yhteensä: {total}")
