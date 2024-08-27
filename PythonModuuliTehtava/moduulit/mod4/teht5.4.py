# 5. Käyttäjä tunnus ja salasana
tunnus = "python"
salasana = "rules"
vuorot = 0

while True:
    if vuorot >= 5:
        print("Pääsy evätty")
        break

    user_tunnus = input("Syötä käyttäjätunnus: ")
    if user_tunnus == tunnus:
        user_salasana = input("Syötä salasana: ")
        if user_salasana == salasana:
            print("Tervetuloa")
            break

    if user_tunnus != tunnus:
        print("Väärä käyttäjätunnus")
    else:
        print("Väärä salasana")

    vuorot = vuorot + 1
