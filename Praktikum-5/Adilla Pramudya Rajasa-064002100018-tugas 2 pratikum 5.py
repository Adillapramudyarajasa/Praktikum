print("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
HARGA TIKET WISATA AIR
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. UMUR 1-2 TAHUN : GRATIS!
2. UMUR 3-12 TAHUN : $14.OO
3. UMUR 13-64 TAHUN :  $23.00
4. UMUR 64 TAHUN KEATAS : $18.00
====================================
TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI !!
      """)
umur = "0"
harga = 0
while True:

    try:
        umur = int(input("SILAKAN MASUKAN UMUR: "))
    except ValueError:
        break
    if(umur <= 2):
       print("==========================================================")
       print("HARGA TIKET GRATIS UNTUK UMUR 2 TAHUN KEBAWAH")
       print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN !!")
       print("==========================================================")
       harga += 0
    elif(umur >= 3 and umur <= 12):
       print("==========================================================")
       print("HARGA TIKET $14.00")
       print(f"TOTAL HARGA SAAT INI : ${harga}")
       print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN !!")
       print("==========================================================")
       harga += 14
    elif(umur >= 65):
       print("==========================================================")
       print("HARGA TIKET $18.00")
       print(f"TOTAL HARGA SAAT INI : ${harga}")
       print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN !!")
       print("==========================================================")
       print("TOTAL HARGA SAAT INI : ")    
       harga += 18
    else:
       print("==========================================================")
       print("HARGA TIKET $23.00")
       print(f"TOTAL HARGA SAAT INI : ${harga}")
       print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN!!")
       print("==========================================================")
       harga += 23
print("HARGA TOTALl",harga)
bayar = int(input("MASUKAN JUMLAH UANG "))
kembalian = bayar - harga
print(f"KEMBALIAN : ${kembalian}")
