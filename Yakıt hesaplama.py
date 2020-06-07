from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class YakitHesaplayici(QDialog):
    def __init__(self, ebeveyn=None, parent=None):
        super(YakitHesaplayici,self).__init__(parent)

        grid=QGridLayout()

        # birinci satır kodu
        grid.addWidget(QLabel("gidilen yol"),0,0)
        self.gidilenyol=QLineEdit()
        self.gidilenyol.setInputMask("00000")
        grid.addWidget(self.gidilenyol,0,1)


        # ikinci satır kodu
        grid.addWidget(QLabel("yakıtın litre fiyatı"),1,0)
        self.yakitfiyati=QLineEdit()
        self.yakitfiyati.setInputMask("0.0")
        grid.addWidget(self.yakitfiyati,1,1)

        #üçüncü satır kodu
        grid.addWidget(QLabel("100 km de tüketilen yakıt"),2,0)
        self.tuketilen = QLineEdit()
        self.tuketilen.setInputMask("00.0")
        grid.addWidget(self.tuketilen,2,1)

        #dördüncü satır
        grid.addWidget(QLabel("toplam tutar:"),3,0)
        self.toplamtutar=QLabel("")
        grid.addWidget(self.toplamtutar,3,1)

        #beşinci satır
        hesapla=QPushButton("hesapla")
        hesapla.clicked.connect(self.hesap)
        grid.addWidget(hesapla,4,0,1,2)

        self.setLayout(grid)
        self.setWindowTitle("Yakıt Hesaplayıcısı")

    def hesap(self):
        yol=int(self.gidilenyol.text())
        fiyat=float(self.yakitfiyati.text())
        tuketim=float(self.tuketilen.text())
        sonuc=fiyat*(yol*tuketim)/100
        self.toplamtutar.setText("<font color='blue'>%0.2f</font>"%sonuc)






app=QApplication([])
pencere=YakitHesaplayici()
pencere.show()
app.exec()












