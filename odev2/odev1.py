maas=float(input("Maaşınızı giriniz: "))

if maas<=10000:
    maas=maas-((maas*5)/100)
elif maas<=25000:
    maas=maas-((maas*10)/100)
elif maas<=45000:
    maas=maas((maas*25)/100)
else:
    maas=maas-((maas*30)/100)

print(f"Yeni maaşınız= {maas}")