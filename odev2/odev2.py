kullanici_adi=input("Kullanıcı adı giriniz: ")
sifre=input("Şifre giriniz: ")

if len(sifre)+1>=6:
    print("Hesabınız oluşturuldu")
else:
    print("Şifre en az 6 haneli olmalı")
