# 2. Tuumat niin pitkään kunnes ei tule negatiivinen
tuuma = float(input("Ilmoita tuumat: "))


while tuuma >= 0:
    print(f"{tuuma * 2.54} cm")
    tuuma = float(input("Ilmoita tuumat uudelleen: "))
