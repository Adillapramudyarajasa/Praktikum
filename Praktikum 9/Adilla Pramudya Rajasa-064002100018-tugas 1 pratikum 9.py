def tulis(n):
    file = open('File_biodata.txt','w')
    file.write(str(n))
    file.close()

def baca():
    file = open('File_biodata.txt','r')
    print(file.read())
    file.close()

A = str(input('masukan nama = '))
B = str(input('masukan umur = '))
C = str(input('masukan alamat = '))
D = str(input('masukan email = '))
E = str(input('masukan nama dosen walimu = '))
bio = str(f'''
Nama = {A}
Umur = {B}
Alamat = {C}
Email = {D}
Dosen Wali = {E}''')

print('\nBerikut Isi Data kamu')
tulis(bio)
baca()
