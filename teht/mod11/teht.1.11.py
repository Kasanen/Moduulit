# 1. Luokkahierakia
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
        
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi} (kirjailija {self.kirjoittaja}, {self.sivumaara} sivua)")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi} (päätoimittaja {self.paatoimittaja})")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for i in julkaisut:
    i.tulosta_tiedot()