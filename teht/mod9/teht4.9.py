import random

# Kilpailu
class Auto:
    def __init__(car, rekisteritunnut, huippunopeus, hetkinennopeus, matka):
        car.rekisteritunnus = rekisteritunnut
        car.huippunopeus = huippunopeus
        car.hetkinennopeus = hetkinennopeus
        car.matka = matka

    def kiihdyta(car, nopeus):
        car.hetkinennopeus += nopeus

        if(car.hetkinennopeus < 0):
            car.hetkinennopeus = 0

        if(car.hetkinennopeus > car.huippunopeus):
            car.hetkinennopeus = car.huippunopeus

    def kulje(car, aika):
        car.matka = car.matka + car.hetkinennopeus * aika

autot = []

for i in range(1,11):
    uusi_auto = Auto(f"ABC-{i}", random.randint(100, 200), 0 , 0)
    autot.append(uusi_auto)

voittaja = False
kierrokset = 0

while voittaja == False:
    print(f"")
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        print(f"{auto.rekisteritunnus}, {auto.huippunopeus}km/h, {auto.hetkinennopeus}km/h, {auto.matka}km")

        if auto.matka > 10000:
            print(f"Voittaja on {auto.rekisteritunnus}!")
            voittaja = True
            break
    if voittaja == True:
        break