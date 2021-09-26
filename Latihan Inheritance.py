class pesawat:
    def __init__(self, warna, tahun, maskapai):
        self.warna = warna
        self.tahun = tahun
        self.maskapai = maskapai

    def printname(self):
        print(self.warna)
        print(self.tahun)
        print(self.maskapai)

class Airbus(pesawat):
    def __init__(self, warna, tahun, maskapai):
        pesawat.__init__(self,warna,tahun,maskapai)
        self.KodeBody = "Kilo"

    def tampilanairbus(self):
        print("Kode Body : ", self.KodeBody)
        print("Maskapai  : ", self.maskapai)
        print("Warna     : ", self.warna)
        print("Tahun     : ", self.tahun)

class Boeing(pesawat):
    def __init__(self, warna, tahun, maskapai):
        pesawat.__init__(self,warna, tahun, maskapai)
        self.KodeBody = "Papa"
 
    def tampilanboeing(self):
        print("Kode Body : ", self.KodeBody)
        print("Maskapai  : ", self.maskapai)
        print("Warna     : ", self.warna)
        print("Tahun     : ", self.tahun)

x = Airbus("Putih",2020,"AirAsia")
y = Boeing("Biru",2019,"Garuda")

x.tampilanairbus()
print("=================")
y.tampilanboeing()