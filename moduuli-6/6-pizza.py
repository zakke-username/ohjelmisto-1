import math


def main():
    diameter1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
    price1 = float(input("Anna ensimmäisen pizzan hinta: "))
    diameter2 = float(input("Anna toisen pizzan halkaisija: "))
    price2 = float(input("Anna toisen pizzan hinta: "))

    price_area1 = price_per_m_sq(diameter1, price1)
    price_area2 = price_per_m_sq(diameter2, price2)

    if price_area1 < price_area2:
        print("Ensimmäinen pizza on halvempi!")
    if price_area1 > price_area2:
        print("Toinen pizza on halvempi!")
    else:
        print("Pizzat ovat samanhintaisia")


def price_per_m_sq(diameter_cm, price):
    r = diameter_cm / 2
    area_sq_cm = math.pi * r ** 2
    area_sq_m = area_sq_cm / 10000
    return price / area_sq_m


main()
