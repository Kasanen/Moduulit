import mysql.connector
# 2. Maakoodi

def hakija(maakoodi):
    heli = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%heliport%'"
    pieni = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%small_airport%'"
    kiinni = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%closed%'"
    vesi = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%seaplane_base%'"
    pallo = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%balloonport%'"
    medium = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%medium_airport%'"
    iso = f"SELECT type FROM airport where iso_country='{maakoodi}' and type LIKE '%large_airport%'"

    kursori = yhteys.cursor()

    kursori.execute(heli)
    kursori.fetchall()
    print(f"Helikopterikenttiä on {kursori.rowcount}")

    kursori.execute(pieni)
    kursori.fetchall()
    print(f"Pieniä lentokenttiä on {kursori.rowcount}")

    kursori.execute(kiinni)
    kursori.fetchall()
    print(f"Kiinni on {kursori.rowcount}")

    kursori.execute(vesi)
    kursori.fetchall()
    print(f"Vesitaso lentokenttiä on {kursori.rowcount}")

    kursori.execute(pallo)
    kursori.fetchall()
    print(f"Kuumailmapallo kenttiä on {kursori.rowcount}")

    kursori.execute(medium)
    kursori.fetchall()
    print(f"Keskisuuria lentokenttiä on {kursori.rowcount}")

    kursori.execute(iso)
    kursori.fetchall()
    print(f"Suuria lentokenttiä on {kursori.rowcount}")



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='assa1221',
         autocommit=True
         )

maakoodi = input("Syötä lentokentän maakoodi: ")
hakija(maakoodi)