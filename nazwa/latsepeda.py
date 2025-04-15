class Sepeda: 

    def __init__(self, warna, jenis, merek):
       self.warna = warna
       self.jenis = jenis
       self.merek = merek 

    def kayuh(self):
        print(" Sepeda bisa di kayuh ")
    def rem(self):
        print("Sepeda bisa direm " )

s1 = Sepeda ("hitam", "Sepeda gunung", "polygon")
print(s1.warna)
print(s1.jenis)
print(s1.merek)
s1.kayuh()
s1.rem()

    
    

