import math

class Bola:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_volume(self):
        return (4 / 3) * math.pi * (self.jari_jari ** 3)

    def hitung_luas_permukaan(self):
        return 4 * math.pi * (self.jari_jari ** 2)


if __name__ == '__main__':
    jari_jari = float(input("Masukkan jari-jari bola: "))
    bola = Bola(jari_jari)
    print("Volume bola:", bola.hitung_volume())
    print("Luas permukaan bola:", bola.hitung_luas_permukaan())
