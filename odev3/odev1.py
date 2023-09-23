pi=float(input("Pi değerini giriniz : "))
yaricap=float(input("Yarıçapı giriniz : "))

def daire():
    alan=pi*(yaricap**2)
    print(f"Daire alanı = {alan}")

daire()