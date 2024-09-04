import random

def main():
    roll = -1
    while roll != 6:
        roll = roll_dice()
        print(roll)

def roll_dice():
    return random.randint(1,6)

main()