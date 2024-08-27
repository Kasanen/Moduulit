# 3. Luvut pienin ja suurin
luku = float(input("Kirjoita luku: "))
suurin = luku
pienin = luku

while True:
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku

    luku = input("Kirjoita luku uudestaan: ")

    if luku == '':
        break
    luku = float(luku)

print(suurin)
print(pienin)