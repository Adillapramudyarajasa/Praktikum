mmq=0
while mmq==0:
       print("Ketik -1 untuk mengakhiri program ")
       bulan= int(input("masukan jumlah bulan (1-12)? "))
       
       if bulan == -1:
            mmq=1
            print("terima kasih atas kontribusi")
       else:
        if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
               if bulan == 2:
                  tahun= int (input("masukan tahun:"))
                  if (tahun%4==0):
                      print("29hari")
                  elif tahun==-1:
                  	break
                  else:
                       print("28hari")
               else:
                   if bulan==1 or bulan==3 or bulan==5 or        bulan==7 or bulan==8 or bulan==10 or bulan==12:
                       print("31hari")
                   else:
                       print("30hari")
        else:
                    print('invalid')
