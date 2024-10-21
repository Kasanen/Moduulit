import random
from tabulate import tabulate

# 4. Autokilpailu
class Auto:
    def __init__(car, rekisteritunnus, huippunopeus, hetkinennopeus, matka):
        car.rekisteritunnus = rekisteritunnus
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

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot = [Auto(f"ABC-{i}", random.randint(100, 200), 0 , 0) for i in range(1, 11)]

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
        return
    
    def tulosta_tilanne(self):
        print(f"\nTunti on kulunut, tilanne on seuraava:")
        for auto in self.autot:
            print(tabulate([[auto.rekisteritunnus, auto.huippunopeus, auto.hetkinennopeus, auto.matka]], headers=["Rekisteritunnus", "Huippunopeus", "Hetkinennopeus", "Matka"], tablefmt="fancy_grid"))
        return
    
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka > self.pituus_km:
                print(f"Voittaja on {auto.rekisteritunnus}!")
                return True
        return False

K = Kilpailu("Suuri romuralli", 8000)
print(K.kilpailu_ohi())
while K.kilpailu_ohi() == False:
    K.tunti_kuluu()
    K.tulosta_tilanne()
