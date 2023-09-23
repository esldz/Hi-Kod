ogrenci_bilgiler={
    "Ahmet" : {
        "Matematik" : 90,
        "Fizik" : 75,
        "Kimya" : 68
    },
    "Elif" : {
        "Matematik" : 93,
        "Fizik" : 71,
        "Kimya" : 78
    },
    "Mehmet" : {
        "Matematik" : 55,
        "Fizik" : 70,
        "Kimya" : 60
    },
    "Ezel" : {
        "Matematik" : 100,
        "Fizik" : 80,
        "Kimya" : 75
    },
    "Esmanur" : {
        "Matematik" : 85,
        "Fizik" : 70,
        "Kimya" : 50
    },
}

ogrenci_adi=input("Öğrenci Adını Giriniz : ")
ders=input("Ders Adını Giriniz : ")

if ogrenci_adi in ogrenci_bilgiler and ders in ogrenci_bilgiler[ogrenci_adi]:
    print(f"{ogrenci_adi} adlı öğrencinin {ders} notu : {ogrenci_bilgiler[ogrenci_adi][ders]}")
else:
    print("Girilen bilgilerle eşleşen öğrenci bulunamadı")