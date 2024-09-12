# Auto luokka kuljettu matka
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

uusi_auto = Auto("ABC-123", 142, 0 , 2000)
uusi_auto.kiihdyta(60)
uusi_auto.kulje(1.5)

print(f"{uusi_auto.rekisteritunnus}, {uusi_auto.huippunopeus}km/h, {uusi_auto.hetkinennopeus}km/h, {uusi_auto.matka}km")