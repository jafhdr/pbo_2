try:
    with open("file.txt", "r") as file:
        num = int(file.readline())
except FileNotFoundError:
    print("Error: file tidak ditemukan!")
except ValueError:
    print("Error: Input tidak valid!")
except:
    print("Error: Terjadi kesalahan saat membaca file!")
