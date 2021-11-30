
"""

print("PROGRAM MEMBUAT FILE")
print("===============================================")

title = str(input("KETIK JUDUL FILE:"))
filename = (f"{title}.txt")
f = open(filename, "w")
f.close()
print("===============================================")
print(f"FILE {filename} TELAH DIBUAT!!")
print("TEKAN x atau 0 untuk menghentikan program")
print("===============================================")

def write(string):
    file = open(f"{title}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.txt", "r")
    teks = file.read()
    print(teks)

baris = True
while baris == True:
    isi = (input(""))
    if isi == "x" or isi == "0":
        print("\nTEKS TELAH DISIMPAN!")
        baris = False
    else:
        write(isi)
        read()
