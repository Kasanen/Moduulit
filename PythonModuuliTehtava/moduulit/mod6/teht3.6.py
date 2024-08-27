# 3. Bensa
gallonit = 0
syote = 0

def muuttaja(maara):
    arvo = maara * 3.785
    return arvo

syote = float(input("Syötä gallonit: "))

while syote > 0:
    gallonit += syote
    syote = float(input("Syötä gallonit: "))

vastaus = muuttaja(gallonit)
print(f"{vastaus} litraa")