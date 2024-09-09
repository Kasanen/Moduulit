import mysql.connector

def hae_työntekijät_sukunimellä(sukunimi):
    sql = f"SELECT Numero, Sukunimi, Etunimi, Palkka FROM Työntekijä where Sukunimi='{sukunimi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

sukunimi = input("Anna sukunimi: ")
hae_työntekijät_sukunimellä(sukunimi)