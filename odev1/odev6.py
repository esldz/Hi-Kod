sayilar="0123456789"
sayilar_list=list(sayilar)
tek_sayilar=[]
cift_sayilar=[]

for i in sayilar_list:
    if int(i)%2==0:
        cift_sayilar.append(i)
    else:
        tek_sayilar.append(i)

print(f"Tek sayılar : {tek_sayilar}\nÇift sayilar : {cift_sayilar}")