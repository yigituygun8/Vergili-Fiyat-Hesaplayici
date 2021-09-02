import time


teknolojik_aletler = "Teknolojik Aletler: Laptop, Masaüstü, Televizyon ve Oyun Konsolu"
print(teknolojik_aletler)

time.sleep(0.5)
print("-"*64)

araclar = "Araçlar: Mercedes ve BMW"
time.sleep(1)
print(araclar)

time.sleep(0.5)
print("-"*40)

beyaz_esya = "Beyaz Eşyalar: Buzdolabı, Bulaşık Makinesi ve Çamaşır Makinesi"
time.sleep(1)
print(beyaz_esya)

time.sleep(0.5)
print("-"*62)

kategori = str(input("Hangi Kategoriye Gitmek İstiyorsunuz? (Teknolojik Aletler / Araçlar / Beyaz Eşya): "))

hangi_teknoloji = "Hangi Teknolojik Aleti Seçmek İstiyorsunuz? (Laptop / Masaüstü / Televizyon / Oyun Konsolu): "
laptop_fiyat = 7000
masaustu_fiyat = 10000
tv_fiyat = 6000
konsol_fiyat = 3000


hangi_arac = "Hangi Aracı Seçmek İstiyorsunuz? (Mercedes / BMW ): "
mercedes_fiyat = 250000
bmw_fiyat = 200000


hangi_esya = "Hangi Beyaz Eşyayı Seçmek İstiyorsunuz? (Buzdolabı / Çamaşır Makinesi / Bulaşık Makinesi): "
buzdolabı_fiyat = 8000
camasır_fiyat = 4000
bulasık_fiyat = 3000


if kategori == "Teknolojik Aletler":
    a = input(hangi_teknoloji)
    if a == "Laptop":
        print("Laptop'un Vergisiz Fiyatı =",laptop_fiyat,"TL")
        vergili_laptop = laptop_fiyat*(118/100)
        time.sleep(1)
        print("Laptop'un Vergili Fiyatı =",vergili_laptop,"TL")
    elif a == "Masaüstü":
        print("Masaüstü'nün Vergisiz Fiyatı =",masaustu_fiyat,"TL")
        vergili_masaustu = masaustu_fiyat*(118/100)
        time.sleep(1)
        print("Masaüstü'nün Vergili Fiyatı =",vergili_masaustu,"TL")
    elif a == "Televizyon":
        print("Televizyon'un Vergisiz Fiyatı =",tv_fiyat,"TL")
        vergili_tv = tv_fiyat*(141/100)
        time.sleep(1)
        print("Televizyon'un Vergili Fiyatı =",vergili_tv,"TL")
    elif a == "Oyun Konsolu":
        print("Oyun Konsolu'nun Vergisiz Fiyatı =",konsol_fiyat,"TL")
        vergili_konsol = konsol_fiyat*(120/100)
        time.sleep(1)
        print("Oyun Konsolu'nun Vergili Fiyatı =",vergili_konsol,"TL")



if kategori == "Araçlar":
    b = input(hangi_arac)
    if b == "Mercedes":
        print("Mercedes'in Vergisiz Fiyatı =",mercedes_fiyat,"TL")
        vergili_mercedes = mercedes_fiyat + (mercedes_fiyat*(130/100))
        time.sleep(1)
        print("Mercedes'in Vergili Fiyatı =",vergili_mercedes,"TL")
    elif b == "BMW" or "Bmw":
        print("BMW'nin Vergisiz Fiyatı =",bmw_fiyat,"TL")
        vergili_bmw = bmw_fiyat + (bmw_fiyat*(130/100))
        time.sleep(1)
        print("BMW'nin Vergili Fiyatı =",vergili_bmw,"TL")



if kategori == "Beyaz Eşya":
    c = input(hangi_esya)
    if c == "Buzdolabı":
        print("Buzdolabı'nın Vergisiz Fiyatı =",buzdolabı_fiyat,"TL")
        vergili_buzdolabı = int(buzdolabı_fiyat*(120/100))
        time.sleep(1)
        print("Buzdolabı'nın Vergili Fiyatı =",vergili_buzdolabı,"TL")
    elif c == "Çamaşır Makinesi":
        print("Çamaşır Makinesi'nin Vergisiz Fiyatı =",camasır_fiyat,"TL")
        vergili_camasir = int(camasır_fiyat*(120/100))
        time.sleep(1)
        print("Masaüstü'nün Vergili Fiyatı =",vergili_camasir,"TL")
    elif c == "Bulaşık Makinesi":
        print("Bulaşık Makinesi'nin Vergisiz Fiyatı =",bulasık_fiyat,"TL")
        vergili_bulasik = int(bulasık_fiyat*(113/100))
        time.sleep(1)
        print("Bulaşık Makinesi'nin Vergili Fiyatı =",vergili_bulasik,"TL")