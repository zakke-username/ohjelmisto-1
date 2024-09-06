airports = {}

def main():
    while True:
        command = input("\nAnna komento (uusi/hae/lopeta): ").lower()
        if command == "uusi":
            new()
        elif command == "hae":
            search()
        elif command == "lopeta":
            return
        else:
            print("Komennot: uusi, hae, lopeta")

def new():
    icao = input("Anna lentokentän ICAO-koodi: ")
    name = input("Anna lentokentän nimi: ")
    if icao not in airports:
        airports[icao] = name
    else:
        print("ICAO-koodilla on jo lentokenttä")

def search():
    icao = input("Hae lentokenttää ICAO-koodilla: ")
    if icao in airports:
        print(f"Löytyi: {airports[icao]}")
    else:
        print("Koodilla ei löytynyt lentokenttää")

main()
