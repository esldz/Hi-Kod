import pandas as pd

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],

"Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],

"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

df = pd.DataFrame(sozluk)
print(df)

kategori = df.loc[1, "Kategori"]
print(kategori)

urun = df.loc[1, "Ürün"]
print(urun)

istenilen_veri = df.loc[4:9, ["Kategori", "Ürün", "Fiyat"]]
print(istenilen_veri)

istenilen_veri2 = df.loc[1:6, "Ürün"]
print(istenilen_veri2)

giyim = df[df["Kategori"] == "Giyim"]["Ürün"]
print(giyim)

ayakkabi = df[df["Kategori"] == "Ayakkabı"]["Ürün"]
print(ayakkabi)

aksesuar = df[df["Kategori"] == "Aksesuar"]["Ürün"]
print(aksesuar)

giyim_300 = df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)]
print(giyim_300)

ayakkabi_600 = df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] > 600)]
print(ayakkabi_600)

aksesuar_100 = df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)]
print(aksesuar_100)