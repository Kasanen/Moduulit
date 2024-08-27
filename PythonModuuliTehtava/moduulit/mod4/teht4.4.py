import random
# 4. Arvaa luku
arpa = random.randint(1,10)
luku = float(input("Arvaa väliltä 1-10 "))

while luku != arpa:
    if luku > arpa:
        print("Liian suuri arvaus")
    elif luku < arpa:
        print("Liian pieni arvaus")
    luku = float(input("Arvaa uudestaan... "))
print("Arvasti oikein!")