def main():
    auto = Auto("ABC-123", 142)
    print(f"Auton rekisteritunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus}")

    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(auto.nopeus)

    auto.kiihdyta(-200)
    print(auto.nopeus)


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
