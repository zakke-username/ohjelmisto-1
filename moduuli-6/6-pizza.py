import math


def main():
    diameter1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
    price1 = float(input("Anna ensimmäisen pizzan hinta: "))
    diameter2 = float(input("Anna toisen pizzan halkaisija: "))
    price2 = float(input("Anna toisen pizzan hinta: "))

    if price_per_m_sq(diameter1, price1) < price_per_sq_m(diameter2, price2):
        print("Ensimmäinen pizza on halvempi!")
    else:
        print("Toinen pizza on halvempi!")


def price_per_m_sq(diameter_cm, price):
    r = diameter_cm / 2
    area_sq_cm = math.pi * r ** 2
    area_sq_m = area_sq_cm / 10000
    return price / area_sq_m


main()