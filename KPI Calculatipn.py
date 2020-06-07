def asepetterkoranı(sepeteeklenen,yapılandonusum):
    sepetterkoranı=sepeteeklenen/(sepeteeklenen+yapılandonusum)
    sepetterkoranı=1-sepetterkoranı
    return sepetterkoranı

def kargooranı(sepeteeklenen,kargoyapılan):
    kargooranısonuc=(kargoyapılan/sepeteeklenen)
    return kargooranısonuc

def mevcutdonusumoranı(alısverisyapansayısı,tıklamasayısı):
    mevcutdonusumoranısonuc= (alısverisyapansayısı/tıklamasayısı)
    return mevcutdonusumoranısonuc
x=int(input("Sepete Eklenen Ürün Sayısı:"))
y=int(input("Yapılan Dönüşüm Sayısı:"))
alısverissepetiterketmeoranı=asepetterkoranı(x,y)
print("Alışveriş Sepeti Terk Etme oranı: %",alısverissepetiterketmeoranı)

z=int(input("Kargo Yapılan Ürün Sayısı:"))
kargooranısonuc=kargooranı(x,z)
print("Kargo Oranı: %",kargooranısonuc)

a=int(input("Alışveriş Yapan Sayısı:"))
b=int(input("Reklamlara Tıklama Sayısı:"))
mevcutdonusumoranısonuc=mevcutdonusumoranı(a,b)
print("Mevcut Dönüşüm Oranı: %",mevcutdonusumoranısonuc)

if(alısverissepetiterketmeoranı<0.15 and kargooranısonuc>0.70 and mevcutdonusumoranısonuc>=0.16):
    print("Firmamız Hedeflerine başarı ile ulaşmıştır..")


else:
    print("Hedefe ulaşılamadı...")