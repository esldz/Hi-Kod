print("KAYIT OLUN")
kayit_kullanici_adi=input("kullanıcı adı : ")
kayit_sifre=input("Şifre :")

sayac=0
print("GİRİŞ")
while sayac<3:
    sifre=input("Şifre : ")
    sayac+=1

    if sifre == kayit_sifre:
        print("Giriş Başarılı")
        break
    else:
        print(f"Şifre yanlış {3-sayac} deneme hakkınız kaldı")

