
import csv

jami_yolovchilar = {}

with open("qatnov.csv", "r", encoding="utf-8") as fayl:
    oqish = csv.DictReader(fayl)

    for qator in oqish:
        yonalish = qator["yonalish"]
        yolovchi = int(qator["yolovchi"])

        if yonalish in jami_yolovchilar:
            jami_yolovchilar[yonalish] += yolovchi
        else:
            jami_yolovchilar[yonalish] = yolovchi

for yonalish, jami in jami_yolovchilar.items():
    print(f"{yonalish}-yo'nalish: {jami} nafar")


with open("jami_yolovchilar.csv", "w", newline="", encoding="utf-8") as fayl:
    ustunlar = ["yonalish", "jami_yolovchi"]

    yozish = csv.DictWriter(fayl, fieldnames=ustunlar)

    yozish.writeheader()

    for yonalish, jami in jami_yolovchilar.items():
        yozish.writerow({
            "yonalish": yonalish,
            "jami_yolovchi": jami
        })
        
