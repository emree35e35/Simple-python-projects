import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.etiket1 = QtWidgets.QLabel("Adı Soyadı ")
        self.etiket3 = QtWidgets.QLabel("Bugunki Personel sayısı")
        self.etiket4 = QtWidgets.QLabel("Personel Devir Hızı")
        self.etiket6 = QtWidgets.QLabel("-------")
        self.etiket7 = QtWidgets.QLabel("Suanki Personel Sayısı Sonuc")

        # LİNE EDİT KISMI

        self.buton = QtWidgets.QPushButton("Hesapla")
        self.butonekle = QtWidgets.QPushButton("Ekle")
        self.butoncikar = QtWidgets.QPushButton("Cikar")


        # LİNE EDİT KISMI
        self.linedit1 = QtWidgets.QLineEdit()

        #  kutu oluşturup yerlerine koyma
        v_box = QtWidgets.QGridLayout()

        v_box.addWidget(self.etiket1, 0, 0)
        v_box.addWidget(self.linedit1, 0, 1)


        v_box.addWidget(self.etiket3, 2, 0)
        v_box.addWidget(self.etiket7, 2, 1)

        v_box.addWidget(self.etiket4, 3, 0)
        v_box.addWidget(self.etiket6, 3, 1)

        v_box.addWidget(self.buton, 4, 0)
        v_box.addWidget(self.butonekle, 4,1)
        v_box.addWidget(self.butoncikar, 4, 2)

        self.setLayout(v_box)
        self.setFixedSize(450, 150)


        #BUTONLARI CONNECT İLE FONKSİYONLARA BAGLAMA
        self.butonekle.clicked.connect(self.ekle)
        self.butoncikar.clicked.connect(self.cikar)
        self.buton.clicked.connect(self.hesapla)

        self.show()
        self.setWindowTitle("Persone hesaplama")

        #Liste oluşturup uzunlugunu bulma
        self.isciler = list()
        iscileruzunlugu = len(self.isciler)
        iscileruzunlugu2 = int(iscileruzunlugu)
        self.etiket7.setText(str(iscileruzunlugu2))


        #İŞE GİREN CIKAN SAYISI
        self.cikar=0
        self.topla=0

    def ekle(self):

        self.isciler.append(self.linedit1.text())
        self.linedit1.clear()
        iscileruzunlugu = len(self.isciler)
        iscileruzunlugu2 = int(iscileruzunlugu)
        self.etiket7.setText(str(iscileruzunlugu2))

        self.topla += 1

    def cikar(self):
        if(self.etiket7.text()=="0"):
            return
        else:
            self.isciler.remove(self.linedit1.text())
            self.linedit1.clear()
            self.iscileruzunlugu = len(self.isciler)
            self.iscileruzunlugu2 = int(self.iscileruzunlugu)
            self.etiket7.setText(str(self.iscileruzunlugu2))
            self.cikar+=1


    def hesapla(self):
        if (self.topla == 0 or self.cikar==0):
            return
        else:
            a=self.topla/self.cikar*100
            self.etiket6.setText(str(a))












app=(QtWidgets.QApplication(sys.argv))

pencere=Pencere()
sys.exit(app.exec_())