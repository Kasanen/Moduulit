# 1. Auto luokka
class Auto:
    def __init__(car, rekisteritunnut, huippunopeus, hetkinennopeus, matka):
        car.rekisteritunnus = rekisteritunnut
        car.huippunopeus = huippunopeus
        car.hetkinennopeus = hetkinennopeus
        car.matka = matka

uusi_auto = Auto("ABC-123", 142, 0, 0)


print(uusi_auto.rekisteritunnus)
print(uusi_auto.huippunopeus)