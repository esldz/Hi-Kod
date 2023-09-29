import numpy as np

sayilar_1 = np.array([1, 2, 3, 4, 5])

indeks = sayilar_1[2]  
print(f"1. index 2 : {indeks}")

slices = sayilar_1[1:4] 
print(f"1. Slice : {slices}")

print("---------------------------------")

sayilar_2 = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

indeks2 = sayilar_2[1, 2] 
print(f"2. index (1, 2) : {indeks2}")

slices2 = sayilar_2[0:2, 1:3]  
print(f"2. Slice {slices2}")

print("---------------------------------")


sayilar_3 = np.array([[[1, 2],
                        [3, 4]],
                        [[5, 6],
                        [7, 8]],
                        [[9, 10],
                        [11, 12]]])

eleman = sayilar_3[1, 0, 1]  
print(f"3. İndex : {sayilar_3}")

slices3 = sayilar_3[0:2, :, 1]  
print(f"3. slice : {slices3}")
