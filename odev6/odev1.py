import numpy as np 

sayilar = np.array([1,2,3,4,5,6,7,8,9])

boyut=sayilar.ndim
uzunluk=sayilar.shape[0]

print(f"Sayiların boyutu : {boyut}\nSayiların uzunluğu : {uzunluk}")