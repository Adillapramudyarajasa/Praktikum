Angka = ""
def OrdinalNumber(x):
    while Angka !=0:
        if (Angka==1):
            return str (Angka)+ "st"
        if (Angka==2):
            return str(Angka)+ "nd"
        if (Angka==3):
            return str(Angka)+ "rd"
        if Angka in range(4,21):
            return str(Angka)+ "th"
        if (Angka==21):
            return str (Angka)+ "st"
        if (Angka==22):
            return str (Angka)+ "nd"
        if (Angka==23):
            return str (Angka)+ "rd"
        else:
            print("error")
    else:
        print("error")
        
Angka = int(input("masukan angka"))
print(OrdinalNumber(Angka))
