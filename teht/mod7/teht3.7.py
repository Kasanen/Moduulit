# 3. Monivalinta
lentokentat = {}

while True:
    print("\n1. Lisää lentokenttä \n2. Hae lentokenttä \n3. Lopeta")
    valinta = int(input("Syötä numero: "))

    # Lopeta
    if valinta == 3:
        break

    # Lentokenttä haku
    elif valinta == 2:
        print("\nLentokenttä haku")
        koodi = input("Syötä ICAO koodi: ")
        if koodi in lentokentat:
            print(f"ICAO koodilla {koodi} löytyi {lentokentat[koodi]} niminen lentokenttä.")
    
    # Lentokentän lisäys
    elif valinta == 1:
        print("\nLisätään lentokenttä!")
        ICAO = input("Syötä ICAO koodi: ")
        lentokentta = input("Syötä lentokenttä: ")
        
        lentokentat[ICAO] = lentokentta