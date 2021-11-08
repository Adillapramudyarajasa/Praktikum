hitung = 0
jawab = "yes"


while(jawab == "yes"):
    inputbulan = int(input("masukan bulan nya: "))
    inputtahun = int(input("masukan tahun nya: "))
    jawab = str(input("ingin lanjut atau tidak: "))
    

    
       
    def hitung_bulan():
    
      if(inputbulan >= 13 or inputbulan <= 0):
          print("tidak termasuk dalam hitungan bulan")
          
      elif(inputbulan == 1 or inputbulan == 3 or inputbulan == 5 or inputbulan == 7 or inputbulan == 8 or inputbulan == 10 or inputbulan == 12):
    	     print(" bulan ini ada 31 hari")
          
      
           
      elif (inputbulan == 2):
      
        if(inputtahun % 4 == 0 and inputbulan == 2):
          print("bulan ini ada 29 hari")
          return
        
        else :
            print("bulan ini ada 28 hari ")
            
      else:
          print("bulan ini ada 30 hari")
        
          
    hitung_bulan()
