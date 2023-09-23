sayi=int(input("Bir sayı girin : "))

def faktoriyel():
    sonuc=1
    for i in range(1,sayi +1):
        sonuc*=i
    print("{} faktöriyel = {}".format(sayi, sonuc))

faktoriyel()