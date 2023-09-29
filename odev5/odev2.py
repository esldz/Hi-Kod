manav = {
    "meyve": {
        "elma": "20",
        "armut": "25",
        "muz": "25",
        "çilek": "35"
    },
    "sebze": {
        "domates": "18",
        "salatalık": "16",
        "patates": "26",
        "havuç": "20"
    }
}

istenilen = input("İstediğiniz ürün kategorisini seçiniz (meyve/sebze): ")
urun = input(f"{istenilen} kategorisinden istediğiniz ürünün adını giriniz: ")

if istenilen in manav and urun in manav[istenilen]:
    fiyat = manav[istenilen][urun]
    print(f"{urun} fiyatı = {fiyat} TL")
else:
    print("Aradığınız ürün bulunamadı.")

print("Kategoriler:")
for kategori in manav:
    print(kategori)

manav["meyve"]["kivi"] = "40"  # Meyveler kategorisine "kivi" eklenir.

print("Kategoriye Kivi Ekledikten Sonra:")
for kategori in manav["meyve"]:
    print(kategori)

if "brokoli" not in manav["sebze"]:
    manav["sebze"]["brokoli"] = "15"  # Sebzeler kategorisine "brokoli" eklenir.

print("Kategoriye Brokoli Ekledikten Sonra:")
for kategori in manav["sebze"]:
    print(kategori)
