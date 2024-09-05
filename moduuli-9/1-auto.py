def main():
    uusi_auto = Auto("ABC-123", 142)
    print(f"Auton rekisteritunnus: {uusi_auto.rekisteritunnus}, huippunopeus: {uusi_auto.huippunopeus}")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.nopeus = 0
            self.matka = 0

main()
