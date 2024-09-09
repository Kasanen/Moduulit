import mysql.connector
from geopy.distance import geodesic as GD
# 3. Geopy
def hae_lentokentta(ICAO1, ICAO2):
    eka = f"SELECT latitude_deg, longitude_deg FROM airport, country WHERE ident='{ICAO1}'"
    toka = f"SELECT latitude_deg, longitude_deg FROM airport, country WHERE ident='{ICAO2}'"

    kursori = yhteys.cursor()
    def eka_f():
        kursori.execute(eka)
        tulos = kursori.fetchall()
        return tulos[1]

    def toka_f():
        kursori.execute(toka)
        tulos = kursori.fetchall()
        return tulos[1]

    print(f"Etäisyys on {GD(eka_f(),toka_f()).km} kilometriä")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='assa1221',
         autocommit=True
         )

ICAO1 = input("Syötä 1. lentokentän ICAO koodi: ")
ICAO2 = input("Syötä 2. lentokentän ICAO koodi: ")
hae_lentokentta(ICAO1, ICAO2)