import json
import requests

# 2. OpenWeather
hakusana = input("Paikkakunta: ")
api_key = "3fe3086ac36a170a9080928b9d4754b0"


# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
koordinaatit = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + "&appid=3fe3086ac36a170a9080928b9d4754b0"

try:
    coord = requests.get(koordinaatit)
    if coord.status_code==200:
        json_coord = coord.json()
        lon = str(json_coord["coord"]["lon"])
        lat = str(json_coord["coord"]["lat"])

    
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

try:    
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json_vastaus["weather"][0]["description"])
        print(round(json_vastaus["main"]["temp"] - 273.15))

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
