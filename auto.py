class Auto:
    def __init__(self, marka_, tipus_, gyartasi_ev_, fogyasztas_=7.5, uzemanyag_ = 50):
        self.marka= marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_
        self.sebesseg = 0
        self.fogyasztas = fogyasztas_
        self.uzemanyag = uzemanyag_
    def __str__(self):
        return f"{self.marka} {self.tipus} ({self.gyartasi_ev}),\
        sebesség: {self.sebesseg} km/h, üzemanyag {self.uzemanyag}"
    
    def gyorsit(self, ertek):
        self.sebesseg += ertek
        if self.sebesseg > 200:
            self.sebesseg = 200

    def fekez(self, ertek):
        self.sebesseg -= ertek
        if self.sebesseg < 0:
            self.sebesseg = 0

    def tankol(self, mennyiseg):
        self.uzemanyag += mennyiseg
        if self.uzemanyag > 50:
            self.uzemanyag = 50

    def utazik(self, tavolsag):
        fogyasztott_uzemanyag = (tavolsag/100) * self.fogyasztas
        if fogyasztott_uzemanyag > self.uzemanyag:
            print("Tankolni kell")
        else:
            print(f"Fogyasztott üzemanyag: {fogyasztott_uzemanyag}")
            self.uzemanyag -= fogyasztott_uzemanyag
                
