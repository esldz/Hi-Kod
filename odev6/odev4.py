import numpy as np

sifirlar = np.zeros((3, 3))
birler = np.ones((3, 3))

birlesik_satir = np.hstack((sifirlar, birler))
birlesik_sutun = np.vstack((sifirlar, birler))

print(f"Sıfırlar dizisi : {sifirlar}\nBirler dizisi : {birler}")
print(f"Birleşik satır : {birlesik_satir}\nBirleşik Satır : {birlesik_sutun} ")
