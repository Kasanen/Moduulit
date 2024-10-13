# 2. Talo
class Hissi:
    def __init__(self, alin_kerros = 1, ylin_kerros = 10, kerros = 1):
        self.alinkerros = alin_kerros
        self.ylinkerros = ylin_kerros
        self.kerros = kerros

    def kerros_ylos(self, kerros):
        kerros = kerros + 1
        return kerros

    def kerros_alas(self, kerros):
        kerros = kerros - 1  
        return kerros

    def siirry_kerrokseen(self, kerrokseen):
        if(kerrokseen < self.ylinkerros):
            while kerrokseen != self.kerros:
                if kerrokseen > self.kerros and self.kerros < self.ylinkerros:
                    self.kerros = self.kerros_ylos(self.kerros)
                elif kerrokseen < self.kerros and self.kerros > self.alinkerros:
                    self.kerros = self.kerros_alas(self.kerros)
                print(self.kerros)
        else:
            print("?")
        return self.kerros

h = Hissi()
print(h.kerros)
h.siirry_kerrokseen(5)
