#contoh 1
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berlari(self):
        print(self.nama, "berlari")
class Singa(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Mengaung")

singaA = Singa("Bitty", 2, "Jowo")
singaA.berlari() 
singaA.bersuara() 