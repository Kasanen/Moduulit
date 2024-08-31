# 2. Nimiohjelma
nimet = set()
nimi = str

def haku(haettava):
    if haettava in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break

    haku(nimi)
    nimet.add(nimi)

print(nimet)