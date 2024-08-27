import random
# 1. Funktio noppa
toisto = 0

def noppa():
    arvo = random.randint(1,6)
    return arvo

while toisto != 6:
    toisto = noppa()
    print(toisto)