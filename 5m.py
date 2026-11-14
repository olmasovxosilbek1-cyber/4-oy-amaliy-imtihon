
import json

try:

    with open("inventar.json", "r", encoding="utf-8") as fayl:
        kitoblar = json.load(fayl)

    mavjud_kitoblar = []

    for kitob in kitoblar:
        nom = kitob["nom"]
        jami = kitob["jami"]
        band = kitob["band"]

        mavjud = jami - band

        print(f"{nom}: {mavjud} ta mavjud")

        mavjud_kitoblar.append({
            "nom": nom,
            "mavjud": mavjud
        })

    with open("mavjud_kitoblar.json", "w", encoding="utf-8") as fayl:
        json.dump(mavjud_kitoblar, fayl, ensure_ascii=False, indent=4)

    print(f"{len(mavjud_kitoblar)} ta yozuv saqlandi.")

except FileNotFoundError:
    print("Xatolik: inventar.json fayli topilmadi!")

except json.JSONDecodeError:
    print("Xatolik: JSON fayl formati noto'g'ri!")

except KeyError as xato:
    print("Xatolik: kerakli ma'lumot topilmadi:", xato)
