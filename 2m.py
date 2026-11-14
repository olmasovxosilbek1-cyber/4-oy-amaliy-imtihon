haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

xavfli_soni=0
yigindi=0

for harorat in haroratlar:

    yigindi+=harorat

    if harorat >-18:
        xavfli_soni +=1

ortacha = yigindi / len(haroratlar)
 
print("Xavfli olchovlar:",xavfli_soni,"ta")
print(f"Ortacha harorat:{ortacha:.2f} *C")