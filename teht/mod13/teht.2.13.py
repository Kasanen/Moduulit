from flask import Flask, request

# 1. ICAO rajapinta
app = Flask(__name__)
@app.route('/alkuluku/<numero>')

def alkuluku(numero):
    numero = float(numero)
    onko = True

    if numero <= 1:
        onko = False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            onko = False

    vastaus = {
        "Number": numero, "isPrime": onko
    }
    return (vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
