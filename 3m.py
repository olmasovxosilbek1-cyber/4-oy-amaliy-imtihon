def chipta_tekshir(kod):

   
    kod = kod.strip()

    if len(kod) != 14:
        return f"{kod}: yaroqsiz"

    if kod[:3] != "UZ-" or kod[7] != "-":
        return f"{kod}: yaroqsiz"

    yil = kod[3:7]
    seriya = kod[8:14]

 
    if not yil.isdigit():
        return f"{kod}: yaroqsiz"

    if not seriya.isalnum():
        return f"{kod}: yaroqsiz"

    if not seriya.isupper() or not seriya.isalnum():
        return f"{kod}: yaroqsiz"

    if not seriya[:2].isalpha() or not seriya[2:].isdigit():
        return f"{kod}: yaroqsiz"

    return f"{kod}: yaroqli | yil: {yil} | seriya: {seriya}"


kodlar = [
    " UZ-2026-AB1234 ",
    "UZ-26-AB1234",
    "UZ-2026-aB1234"
]

for kod in kodlar:
    print(chipta_tekshir(kod))
    
