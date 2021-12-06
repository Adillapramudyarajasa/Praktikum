class mahasiswatrisakti:

    jumlah = 0

    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        mahasiswatrisakti.jumlah += 1

    def biodata(self):
        return str(f'{self.nama} ; {self.nim} ; {self.tahun}')

    def JMLHDATA(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah sekarang adalah {mahasiswatrisakti.jumlah} orang\nPRESS ENTER')


while True:
    print(f'\nmahasiswatrisakti KE {(mahasiswatrisakti.jumlah)+1}\nKetik exit untuk mengakhiri!')
    x = str(input('MASUKAN Nama: '))
    if x == 'exit':
        break
    y = str(input('MASUKA NIM: '))
    z = str(input('MASUKAN ANGKATAN: '))
    n = mahasiswatrisakti(x,y,z)

    n.JMLHDATA()
