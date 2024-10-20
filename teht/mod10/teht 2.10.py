# 2. Talo
class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def kerros_ylos(self):
        if self.kerros < self.ylinkerros:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alinkerros:
            self.kerros -= 1  

    def siirry_kerrokseen(self, kerrokseen):
        if kerrokseen < self.alinkerros or kerrokseen > self.ylinkerros:
            print("?")
            return self.kerros

        while kerrokseen != self.kerros:
            if kerrokseen > self.kerros:
                self.kerros_ylos()
            elif kerrokseen < self.kerros:
                self.kerros_alas()
        return self.kerros
    
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hisseja):
        self.alinkerros = alin_kerros
        self.ylinkerros = ylin_kerros
        self.hisseja = hisseja
        #Hissien määrittely
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for i in range(hisseja)]

    def aja_hissia(self, hissi_nro, kerrokseen):
        self.hissit[hissi_nro].siirry_kerrokseen(kerrokseen)
        return

t = Talo(1, 10, 3)

t.aja_hissia(1, 4)
t.aja_hissia(2, 10)

print(t.hissit[0].kerros)
print(t.hissit[1].kerros)
print(t.hissit[2].kerros)