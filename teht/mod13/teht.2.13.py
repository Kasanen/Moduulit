import mysql.connector
from flask import Flask

# 1. ICAO rajapinta
def hae_lentokentta(ICAO):
    sql = f"SELECT airport.name, airport.municipality FROM airport WHERE ident='{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        return tulos[0]
    else:
        return None

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True
         )

# Rajapinta
app = Flask(__name__)
@app.route('/kentta/<ICAO>')

def koodi(ICAO):
    lentokentta = hae_lentokentta(ICAO)
    vastaus = {
        "ICAO": ICAO, "Name": lentokentta[0], "Municipality": lentokentta[1],
    }
    return (vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
