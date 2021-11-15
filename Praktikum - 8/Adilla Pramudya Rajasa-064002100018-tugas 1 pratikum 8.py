def fib(n):
  if n <= 1:
      return n
  else:
      return (fib(n-1) + fib(n-2))
  
def cek(x):
    if x <= 0:
        print("bilangan positf")
    else:
        print("Bilangan FIBBONACI ke-",str(x),"adalah",fib(x))
        
while True:
    try:
        bil= int(input("Masukan Bilangan :"))
    except ValueError:
        print("Gagal, Harus bilangan postif/n")
    else:
        cek(bil)
