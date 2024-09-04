def main():
    gal = float(input("Anna gallonat: "))
    while gal >= 0:
        print(f"Litroissa: {gal_to_l(gal)}")
        gal = float(input("Anna gallonat: "))

def gal_to_l(gal):
    return gal * 3.785

main()