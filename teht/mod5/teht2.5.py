# 2. Suuremmasta pienempään
luvut = []
syote = input("Syötä luku: ")

while True:
    syote = input("Syötä luku: ")

    if syote == "":
        break

    luku = int(syote)
    luvut.append(luku)



luvut.sort(reverse=True)
print(luvut[4:])