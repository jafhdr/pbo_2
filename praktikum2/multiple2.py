#contoh 5
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
class Dosen(Person):
    def __init__(self, nama, umur, jurusan):
        self.jurusan = jurusan
    def display_info(self):
        super().display_info()
        print(f"Jurusan: {self.jurusan}")
class Pengampu(Person):
    def __init__(self, nama, umur, tahun_ajar):
        super().__init__(nama, umur)
        self.tahun_ajar = tahun_ajar
    def display_info(self):
        super().display_info()
        print(f"Tahun ajar: {self.tahun_ajar}")
class DosenPengampu(Dosen, Pengampu):
    def __init__(self, nama, umur, jurusan, tahun_ajar):
        Dosen.__init__(self, nama, umur, jurusan)
        Pengampu.__init__(self, nama, umur, tahun_ajar)
    def display_info(self):
        super().display_info()
        print(f"Tahun ajar: {self.tahun_ajar}")
# contoh penggunaan
dosen_pengampuA = DosenPengampu("Budi", 20, "Informatika", 2022)
dosen_pengampuA.display_info()
