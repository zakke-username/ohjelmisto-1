import random

points = int(input("Anna pisteiden määrä: "))
inside_circle = 0

for i in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        inside_circle += 1

print(f"Piin likiarvo: {4 * inside_circle / points}")
