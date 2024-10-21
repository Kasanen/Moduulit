import random

# 2. Luokkahierakia autot
class Auto:
    def __init__(car, rekisteritunnus, huippunopeus):
        car.rekisteritunnus = rekisteritunnus
        car.huippunopeus = huippunopeus

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akun_kapasiteetti):
        self.akun_kapasiteetti = akun_kapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
        self.nopeus = random.randint(1, self.huippunopeus)

    def tulosta_tiedot(self):
        print(f"{self.nopeus * 3} km")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, polttoaineen_tilavuus):
        self.polttoaineen_tilavuus = polttoaineen_tilavuus
        super().__init__(rekisteritunnus, huippunopeus)
        self.nopeus = random.randint(1, self.huippunopeus)

    def tulosta_tiedot(self):
        print(f"{self.nopeus * 3} km")

autot = []
autot.append(Sahkoauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

for i in autot:
    i.tulosta_tiedot()