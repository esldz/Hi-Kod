import datetime

def emekli(isim, dg):
    def yas_hesapla(dg):
        yil = datetime.datetime.now().year
        yas = yil - dg
        return yas

    yasi = yas_hesapla(dg)

    if yasi >= 65:
       print(f"{isim} emekli oldunuz.")
    else:
        kalan_yil = 65 - yasi
        print(f"{isim} emekliliğinize {kalan_yil} yıl kaldı.")

isim = input("İsminiz Giriniz : ")
dg = int(input("Doğum yılınızı Giriniz : "))

emekli(isim, dg)
