import random


def main():
    autolista = []
    for i in range(10):
        a = Auto(f"ABC-{i+1}", random.randint(100,200))
        autolista.append(a)

    kisa = Kilpailu("Suuri romuralli", 8000, autolista)
    tunnit = 0
    while True:
        kisa.tunti_kuluu()
        if tunnit % 10 == 0:
            print(f"\nTilanne tunnilla {tunnit}:")
            kisa.tulosta_tilanne()
        if kisa.kilpailu_ohi():
            print("\nKilpailu ohi! Lopputulos:")
            kisa.tulosta_tilanne()
            return
        tunnit += 1


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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10,15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print("\n")
            print(f"Rekisteritunnus: {auto.rekisteritunnus}")
            print(f"Huippunopeus: {auto.huippunopeus} km/h")
            print(f"Nopeus lopussa: {auto.nopeus} km/h")
            print(f"Kuljettu matka: {auto.matka} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


main()
