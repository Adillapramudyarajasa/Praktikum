def cekbilangan(bil):
    if bil == 1:
        print(f"bilangan {bil} merupakan bilangan prima")
    elif bil == 2:
        print(f"bilangan {bil} merupakan bilangan prima")
    else:
        global x 
        for x in range(2, bil):
            if bil%x==0:
                stat = 0 
                break
            else:
                stat = 1 
        cekstat(stat)
        
def cekstat(stat):
    if stat == 0:
        print(f"bilangan {bil} merupakan bilangan prima")
        print(f"{x} kali {bil//x} = {bil}")
    else:
        print(f"{bil} merupakan bilangan prima")

a = 1
while a == 1:                    
    bil = int(input("masukan angkanya : "))
    cekbilangan(bil)                 
bil = int(input("masukan angkanya : "))
cekbilangan(bil)
