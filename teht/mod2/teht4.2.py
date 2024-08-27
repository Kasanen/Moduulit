# 4. Kokonaisluvun toimenpiteitä
luku1 = input("Kirjoita 1. kokonaisluku: ")
luku2 = input("Kirjoita 2. kokonaisluku: ")
luku3 = input("Kirjoita 3. kokonaisluku: ")
ekaluku = float(luku1)
tokaluku = float(luku2)
kolmasluku = float(luku3)

summa = ekaluku + tokaluku + kolmasluku
tulo = ekaluku * tokaluku * kolmasluku
keskiarvo = summa / 3

print(f"Summa = {summa}")
print(f"Tulo = {tulo}")
print(f"Keskiarvo = {keskiarvo}")