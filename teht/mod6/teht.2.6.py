import random
# 2. Nopan tahkot
toisto = 0
tahkoja = 0
tahkot = int(input("Syötä tahkojen määrä: "))

def noppa():
    arvo = random.randint(1,tahkot)
    return arvo

while toisto != tahkot:
    toisto = noppa()
    tahkoja += tahkot
    print(tahkoja)