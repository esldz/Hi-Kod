import numpy as np

sayilar = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

boyut=sayilar.ndim
uzunluk=sayilar.size
satir, sutun=sayilar.shape

print(f"Sayiların boyutu : {boyut}\nSayiların uzunluğu : {uzunluk}\nSayiların satır sayısı : {satir}\nSayiların sutün sayısı : {sutun}")

indexle = sayilar[1, 1] 
print(f"Sayiların (1, 1) : {indexle}")

slicele=sayilar[0:2, 1:3]
print(f"0 ve 1. satırlar, 1 ve 2. sütunlardaki sayılar : {slicele}")
