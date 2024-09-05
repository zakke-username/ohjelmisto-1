def main():
    hissi = Hissi(1,6)
    hissi.siirry_kerrokseen(4)
    print(hissi.kerros)
    hissi.siirry_kerrokseen(1)
    print(hissi.kerros)


class Hissi:
    def __init__(self, alin, ylin):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kerros):
        ero = abs(self.kerros - kerros)
        if kerros > self.kerros:
            for i in range(ero):
                self.kerros_ylos()
        elif kerros < self.kerros:
            for i in range(ero):
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros = max(self.alin_kerros, min(self.kerros+1, self.ylin_kerros))

    def kerros_alas(self):
        self.kerros = max(self.alin_kerros, min(self.kerros-1, self.ylin_kerros))


main()
