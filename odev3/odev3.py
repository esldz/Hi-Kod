import datetime

def yil(dg):
    yil = datetime.datetime.now().year
    yas = yil - dg
    print(f"Girilen doğum yılı bilgisine göre yaşınız {yas}")

dg=int(input("Doğum yılınızı giriniz : "))

yil(dg)