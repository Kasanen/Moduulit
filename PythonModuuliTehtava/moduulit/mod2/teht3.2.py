# 3. Suorakulmion piiri ja pinta-ala
kanta_str = input("Suorakulmion kanta: ")
korkeus_str = input("Suorakulmion korkeus: ")
kanta = float(kanta_str)
korkeus = float(korkeus_str)

print(f"Suorakulmion piiri on {(kanta*2) + (korkeus*2)} ja pinta-ala on {kanta * korkeus}")