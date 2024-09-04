import random

def main():
    sides = int(input("Anna nopan tahkot: "))
    roll = -1
    while roll != sides:
        roll = roll_dice(sides)
        print(roll)

def roll_dice(sides):
    return random.randint(1,sides)

main()