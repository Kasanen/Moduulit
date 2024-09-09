import mysql.connector
# 1. ICAO
def hae_lentokentta(ICAO):
    sql = f"SELECT airport.name, country.name FROM airport, country WHERE ident='{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print({tulos[1]})

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='assa1221',
         autocommit=True
         )

ICAO = input("Syötä lentokentän ICAO koodin: ")
hae_lentokentta(ICAO)