# 4. Karkausvuosi
vuosi = float(input("Ilmoita vuosi: "))

if vuosi % 4 == 0 or vuosi % 400 == 0:
    print("Vuosi on karkausvuosi")
