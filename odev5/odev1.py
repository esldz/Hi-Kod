ogrenciler={
    "Ali":{
        "Matematik" : 90,
        "Fizik" : 80,
        "Kimya" : 75
    },
    "Ahmet":{
        "Matematik" : 95,
        "Fizik" : 90,
        "Kimya" : 80
    },
    "Esin":{
        "Matematik" : 100,
        "Fizik" : 70,
        "Kimya" : 85
    },
    "Zehra":{
        "Matematik" : 80,
        "Fizik" : 95,
        "Kimya" : 60
    },
    "Pelin":{
        "Matematik" : 70,
        "Fizik" : 95,
        "Kimya" : 65
    },
}

ad=input("Öğrenci adı girin : ")
ders=input("Ders adı girin : ")

if ad in ogrenciler and ders in ogrenciler[ad]:
    notu = ogrenciler[ad][ders]
    print(f"{ad} adlı öğrencinin {ders} notu {notu} .")
else:
    print("Bilgilerle eşleşen öğrenci bulunamadı.")