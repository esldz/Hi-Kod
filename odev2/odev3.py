kullanici_adi=input("Kullanıcı adı giriniz: ")
while True:
    sifre=input("Şifre giriniz: ")
    
    if 10>= len(sifre)+1 >=5:
        print("Hesabınız oluşturuldu")
        break
    else:
        print("Şifre en az 5 en fazla 10 haneli olmalıdır!")
        continue
