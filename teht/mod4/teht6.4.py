import random
# 6. Piin likiarvon laskeminen
N = 0
vuoro = 0

pisteet = float(input("Anna pisteiden lukumäärä: "))

while vuoro < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        N = N + 1
    
    vuoro = vuoro + 1

likiarvo = 4 * N / pisteet
print(f"Piin likiarvo {pisteet} pisteellä on: {likiarvo}")