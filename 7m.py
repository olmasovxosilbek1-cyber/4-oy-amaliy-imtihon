
import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]

ortacha = sum(sarf) / len(sarf)

yuqori_kunlar = []
yuqori_sarf = []

for i in range(len(sarf)):
    if sarf[i] > ortacha:
        yuqori_kunlar.append(kunlar[i])
        yuqori_sarf.append(sarf[i])

print(f"O'rtacha sarf: {ortacha:.2f} kWh")
print("O'rtachadan yuqori kunlar:", ", ".join(yuqori_kunlar))

plt.figure(figsize=(10, 5))

plt.plot(kunlar, sarf, marker="o", label="Elektr sarfi")

plt.axhline(
    y=ortacha,
    color="red",
    linestyle="--",
    label=f"O'rtacha: {ortacha:.2f} kWh"
)

plt.scatter(
    yuqori_kunlar,
    yuqori_sarf,
    color="red",
    s=100,
    label="O'rtachadan yuqori"
)

plt.title("7 kunlik energiya sarfi tahlili")
plt.xlabel("Hafta kunlari")
plt.ylabel("Elektr sarfi (kWh)")
plt.legend()
plt.grid(True)

plt.savefig("energiya_tahlili.png")
plt.show()
