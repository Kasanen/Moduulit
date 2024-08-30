# 1. Vuodenajat
vuodenajat = {"12"or"1"or"2":"talvi",
              "3"or"4"or"5":"kevät",
              "6"or"7"or"8":"kesä",
              "9"or"10"or"11":"syksy"}

kuukausi = str(input("Syötä kuukauden numero: "))
if kuukausi in vuodenajat:
    print(vuodenajat[kuukausi])
