while(True):
    print(" ")
    print("Üretim menüsüne hoş geldiniz...")
    print("-------------------------")
    a = int(input("Adet Sayısını Giriniz:"))
    b = int(input("Malzeme Giderini Giriniz:"))
    c = int(input("İşçilik Giderini Giriniz:"))
    d = int(input("Değişken Genel Üretim Giderini Giriniz:"))
    e = int(input("Sabit Direkt Genel Üretim Giderini Giriniz:"))
    f = int(input("Sabit Ortak Genel Üretim Giderini Giriniz:"))


    def uretme(adet, malzemeg, iscilikg, degiskengenelüretimg, sabitdirektgenelüretimg, sabitortakgenelüretimg):
        degiskengenelüretimg = degiskengenelüretimg * adet


        malzemegideri = malzemeg * adet

        toplam = iscilikg + malzemegideri + degiskengenelüretimg + sabitdirektgenelüretimg + sabitortakgenelüretimg
        return toplam

    uretimsonuc = uretme(a, b, c, d, e, f)
    print("-------------------------")
    print("Üretim işleminde toplam gider:", uretimsonuc)
    print(" ")
    print(" ")
    print("Satınalma menüsüne hoş geldiniz...")
    print("*************************")
    g = int(input("Satın Alınıcak ürünün fiyatını giriniz:"))
    h = int(input("Adet Sayısını Giriniz:"))


    def satınalma(satınalma, adet):
        satınalım = satınalma * adet
        return satınalım
    satınalmasonuc = satınalma(g, h)
    print("-------------------------")
    print("Satın alma işleminde toplam gider:", satınalmasonuc)
    print("*************************")
    break
if (satınalmasonuc > uretimsonuc):
    print("*************************")
    print("*************************")
    print("KARAR!!")
    print("Üretim kararı vermek daha az maliyetli olur")
    print("*************************")
    print("*************************")
else:
    print("*************************")
    print("*************************")
    print("KARAR!!")
    print("Satınalma kararı vermek daha az maliyetli olur")
    print("*************************")
    print("*************************")