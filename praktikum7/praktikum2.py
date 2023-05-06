import math

class Silinder:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        return math.pi * (self.jari_jari ** 2) * self.tinggi

    def hitung_luas_permukaan(self):
        luas_selimut = 2 * math.pi * self.jari_jari * self.tinggi
        luas_tutup_atas = math.pi * (self.jari_jari ** 2)
        luas_tutup_bawah = luas_tutup_atas
        return 2 * luas_tutup_atas + luas_tutup_bawah + luas_selimut


if __name__ == '__main__':
    jari_jari = float(input("Masukkan jari-jari silinder: "))
    tinggi = float(input("Masukkan tinggi silinder: "))
    silinder = Silinder(jari_jari, tinggi)
    print("Volume silinder:", silinder.hitung_volume())
    print("Luas permukaan silinder:", silinder.hitung_luas_permukaan())
