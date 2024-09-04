import random

dice = int(input("Kuinka monta noppaa heitetään? "))
total = 0
for i in range(dice):
    roll = random.randint(1,6)
    total += roll

print(f"Tulos yhteensä: {total}")