# 5. Massa laskuri
leiviskät = input("Anna leiviskät: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")
leiviskä_kpl = float(leiviskät)
naula_kpl = float(naulat)
luoti_kpl = float(luodit)

luoti = 13.3
naula = luoti * 32
leiviskä = naula * 20

arvo = leiviskä_kpl * leiviskä + naula_kpl * naula + luoti_kpl * luoti
kg = int(arvo//1000)
LPArvo = int(arvo % 1000)

print(f"{kg} kilogrammaa ja {LPArvo} grammaa.")