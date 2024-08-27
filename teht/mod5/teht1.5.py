import random
# 1. Arpakuutiot
kuutio = random.randint(1,6)
kerta = 0
summa = 0
arvat = []
arpaMaara = float(input("Ilmoita arpakuutioiden lukumäärä: "))


while kerta < arpaMaara:
    arvat.append(kuutio)
    kerta += 1

for luku in arvat:
    summa = summa + luku

print(f"Arpakuutioiden silmälukujen summa on {summa}") 