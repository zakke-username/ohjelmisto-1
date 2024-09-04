import math

seasons = ("talvi", "kevät", "kesä", "syksy")
month = int(input("Anna kuukauden numero: "))
if month == 12: month = 0

print(f"Vuodenaika: {seasons[math.floor(month / 3)]}")
