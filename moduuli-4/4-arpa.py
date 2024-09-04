import random

roll = random.randint(1,10)
guess = -1

while guess != roll:
    guess = int(input("Arvaa numero väliltä 1-10: "))

    if guess < roll:
        print("Liian pieni")
    elif guess > roll:
        print("Liian iso")
    else:
        print("Oikein!")
