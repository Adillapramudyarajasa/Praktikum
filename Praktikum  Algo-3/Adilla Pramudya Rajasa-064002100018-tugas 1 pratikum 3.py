print("menentukan jenis segitiga")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
a = int(input("masukan angkanya sisi a : "))
b = int(input("masukan angkanya sisi b : "))
c = int(input("masukan angkanya sisi c: "))


if a == b and b == c : 
    print("segitiga sama sisi : ")
elif (a + b <= c ) or ( a + c <= b ) or ( b + c <= a ) :
    print(" bukan segitiga")
elif a == b or b == c or a == c :
    print("segitiga sama kaki : ")
elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a :
    print("segitiga siku siku")

else: 
    print("segitga sembarang")
© 2021 GitHub, Inc.
Terms
Privacy
