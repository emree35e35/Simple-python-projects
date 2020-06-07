import random
import time

class Remote_control():
    def __init__(self,Tv="Off",TvSound=0,ChannelList=["Trt","Atv","Show"],Channel="Trt"):
        self.Tv=Tv
        self.TvSound=TvSound
        self.ChannelList=ChannelList
        self.Channel=Channel

    def TvOn(self):
        if(self.Tv=="Off"):
            print("Television is turning On...")
            time.sleep(1)
            self.Tv="On"
            print("Television is On.")
        else:
            print("Television is already On.")
    def TvOff(self):
        if(self.Tv=="On"):
            print("Television is turning Off")
            time.sleep(1)
            self.Tv="Off"
            print("Television's off.")
        else:
            print("Television is already Off.")
    def TvSes(self):
       while True:
           print("Ses arttırmak icin '>', Azaltmak için '<' Çıkmak için q basın.")
           cevap2=input("Giriniz:")
           if (cevap2==">"):
               if (self.TvSound != 31):
                    print("Ses arttırılıyor")
                    self.TvSound +=1
                    print(self.TvSound)
               else:
                   print("Ses Daha fazla Arttırılamıyor")
           elif (cevap2 == "<"):
               if(self.TvSound !=0):
                   print("Ses Azaltılıyor")
                   self.TvSound -= 1
                   print(self.TvSound)
               else:
                   print("Ses Daha fazla Azaltılamıyor")
           elif (cevap2 == "q"):
               print("Çıkış yapılıyor")
               time.sleep(1)
               break
    def Kanalekle(self):
       while True:
           Yenikanal=input("Eklemek istediginiz Kanal adını Giriniz veya Çıkmak için 'q' basınız:")
           if(Yenikanal=="q"):
               print("Çıkış yapılıyor...")
               time.sleep(1)
               break
           else:
               print("Kanal ekleniyor...")
               time.sleep(1)
               self.ChannelList.append(Yenikanal)
               print(self.ChannelList)
    def __len__(self):
        return len(self.ChannelList)
    def __str__(self):
        return """
        Tvdurum : {}
        TvSes : {}
        Kanal Listesi : {}
        Şuanki Kanal : {}



        """.format(self.Tv,self.TvSound,self.ChannelList,self.Channel)
    def rastgelekanal(self):
        rastgele=random.randint(0,len(self.ChannelList)-1)
        self.Channel=self.ChannelList[rastgele]
        print(self.Channel)




Remote=Remote_control()
print("""
1.Tv AÇ

2.TV Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal sayısını öğrenme

6.Rastgele kanala geçme

7.Televizyon Bilgileri

Çıkmak için "q" basınız.
""")


while(True):
    cevap = input("Answer:")
    if (cevap=="q"):
        print("Program kapatılıyor...")
        time.sleep(1)
        break
    elif(cevap=="1"):
        Remote.TvOn()
    elif(cevap=="2"):
        Remote.TvOff()
    elif (cevap == "3"and Remote.Tv=="On"):
        Remote.TvSes()
    elif (cevap=="4"and Remote.Tv=="On"):
        Remote.Kanalekle()
    elif (cevap=="5"and Remote.Tv=="On"):
        print("Kanal Sayısı:",len(Remote))
    elif (cevap=="6"and Remote.Tv=="On"):
        Remote.rastgelekanal()
    elif (cevap=="7"):
        print("Bilgiler")
        print(str(Remote))
    else:
        print("Geçersiz Giriş veya İşlem Yapmadan Önce Televizyonu Açınız")