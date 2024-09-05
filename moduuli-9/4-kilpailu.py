import random

def main():
    autot = []

    for i in range(10):
        rekisteri = f"ABC-{i+1}"
        huippu = random.randint(100,200)
        uusi_auto = Auto(rekisteri, huippu)
        autot.append(uusi_auto)

    while True:
        maalissa = False
        for auto in autot:
            auto.kiihdyta(random.randint(-10,15))
            auto.kulje(1)
            if auto.matka >= 10000:
                maalissa = True
        if maalissa:
            break

    for auto in autot:
        print("\n")
        print(f"Rekisteritunnus: {auto.rekisteritunnus}")
        print(f"Huippunopeus: {auto.huippunopeus} km/h")
        print(f"Nopeus lopussa: {auto.nopeus} km/h")
        print(f"Kuljettu matka: {auto.matka} km")


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.nopeus = 0
            self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus


main()
