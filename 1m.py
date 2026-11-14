log="hall-a,hall-b,hall-a,hall-c,hall-a,hall-b"

bolimlar = log.split(",")

tozalangan = []

for bolim in bolimlar:
    bolim = bolim.strip()

    if bolim != "":
        tozalangan.append(bolim.upper())

print("Tozalangan:", ", ".join(tozalangan))

noyob_bolimlar = set(tozalangan)

print("Noyob bo'limlar:", len(noyob_bolimlar))
