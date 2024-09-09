import math

seasons = ("talvi", "kevät", "kesä", "syksy")
month = int(input("Anna kuukauden numero: "))
if month == 12: month = 0
season = seasons[math.floor(month/3)]

print(f"Vuodenaika: {season}")
