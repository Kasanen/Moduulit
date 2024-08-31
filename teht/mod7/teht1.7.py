# 1. Vuodenajat
vuodenajat = {"12":"Tavli", "1":"Talvi", "2":"Talvi",
              "3":"Kevät", "4":"Kevät", "5":"Kevät",
              "6":"Kesä", "7":"Kesä", "8":"Kesä",
              "9":"Syksy", "10":"Syksy", "11":"Syksy"}

kuukausi = str(input("Syötä kuukauden numero: "))
if kuukausi in vuodenajat:
    print(vuodenajat[kuukausi])
