# 3. Hemoglobiinin arvot
sukupuoli = input("Ilmoita sukupuolesi: ").upper()
hemoglobiini = float(input("Ilmoita hemoglobiiniarvon: "))

if sukupuoli == "NAINEN":
    if 117 <= hemoglobiini <= 175:
        print(f"Hemoglobiini normaali {hemoglobiini}g/l")
    elif hemoglobiini < 117:
        print(f"Hemoglobiini alhainen {hemoglobiini}g/l")
    elif hemoglobiini > 175:
        print(f"Hemoglobiini korkea {hemoglobiini}g/l")

if sukupuoli == "MIES":
    if 134 <= hemoglobiini <= 195:
        print(f"Hemoglobiini normaali {hemoglobiini}g/l")
    elif hemoglobiini < 134:
        print(f"Hemoglobiini alhainen {hemoglobiini}g/l")
    elif hemoglobiini > 195:
        print(f"Hemoglobiini korkea {hemoglobiini}g/l")
