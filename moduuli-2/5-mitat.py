import math


leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = 0
grammat += leiviskat * 20 * 32 * 13.3
grammat += naulat * 32 * 13.3
grammat += luodit * 13.3

kilogrammat = math.floor(grammat / 1000)
grammat_yli = round(grammat % 1000)

print(f"Massa nykymitoissa: {kilogrammat} kilogrammaa ja {grammat_yli} grammaa")
