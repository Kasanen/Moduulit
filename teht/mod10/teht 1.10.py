# 1. Hissi
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, kerros = 1):
        self.alinkerros = alin_kerros
        self.ylinkerros = ylin_kerros
        self.kerros = kerros
        
class Siirtyminen:
    def kerros_ylos(self, kerrokset):
        kerrokset.kerros += 1

    def kerros_alas(self):
        kerrokset.kerros -= 1   

    def siirry_kerrokseen(self, kerrokset, kerros):
        while kerrokset.kerros != kerros:
            if kerrokset.kerros < kerros:
                self.kerros_ylos(kerros)
            elif kerrokset.kerros > kerros:
                self.kerros_alas(kerros)
            print(kerrokset.kerros)
        return kerrokset.kerros 

h = Siirtyminen()
kerrokset = Hissi(1, 10)
print(kerrokset.kerros)
h.siirry_kerrokseen(kerrokset, 5)
print(kerrokset.kerros)