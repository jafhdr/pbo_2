#contoh 2
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")
class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def makan(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang makan.")
dosenA = Dosen("JafHDr", 35, "123456")
dosenA.berbicara() 
dosenA.makan() 