class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3

    def hitung_luas_permukaan(self):
        return 6 * (self.sisi ** 2)


if __name__ == '__main__':
    sisi = float(input("Masukkan panjang sisi kubus: "))
    kubus = Kubus(sisi)
    print("Volume kubus:", kubus.hitung_volume())
    print("Luas permukaan kubus:", kubus.hitung_luas_permukaan())
