def main():
    talo = Talo(1,7,3)
    talo.aja_hissia(1,4)
    talo.aja_hissia(2, 3)
    talo.aja_hissia(3, 999)

    for h in talo.hissit:
        print(h.kerros)


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, num_hissit):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(num_hissit):
            h = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(h)

    def aja_hissia(self, hissi_nro, kerros):
        h = self.hissit[hissi_nro-1]
        h.siirry_kerrokseen(kerros)


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
