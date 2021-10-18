skor = 0    
nsiswa = list() 

ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    x = str(input('"KELUAR" untuk mengakhiri!\nNilai siswa: ')) 
    if x == 'KELUAR': 
        ulang = 1
    else: 
        if x == 'A': 
            skor = float(4.00)
        elif x == 'A-':
            skor = float(3.75)
        elif x == 'B+':
            skor = float(3.50)
        elif x == 'B':
            skor = float(3.00)
        elif x == 'B-':
            skor = float(2.75)
        elif x == 'C+':
            skor = float(2.50)
        elif x == 'C':
            skor = float(2.00)
        elif x == 'C-':
            skor = float(1.75)
        elif x == 'D':
            skor = float(1.50)
        elif x == 'E':
            skor = float(1.25)
        else:
            print('Saya tidak mengerti...')
            skor = 0
        print(('\nNilai ke-{0} = {1}').format(nomor,skor))
        nsiswa.append(skor)
    
rata2 = sum(nsiswa) / len(nsiswa) # total / jumlah = rata2
print('Rata ratanya n:', rata2)
