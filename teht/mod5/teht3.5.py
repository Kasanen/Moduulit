# 3. Alkuluku ohjelma
luku = int(input("Kirjoita kokonaisluku: "))
alkuluku = True
muut = int(luku**0.5) + 1 

for vastaus in range(2,muut):
    if luku % vastaus == 0:
        alkuluku = False

if alkuluku == True:
    print(f"{luku} on alkuluku!")
else:
    print(f"{luku} ei ole alkuluku!")