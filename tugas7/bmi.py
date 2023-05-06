from functools import wraps

def validate_input(func):
    @wraps(func)
    def wrapper(height, weight):
        if height <= 0 or weight <= 0:
            raise ValueError("Tinggi dan berat badan harus lebih besar dari nol.")
        return func(height, weight)
    return wrapper

def calculate_bmi(height, weight):
    return weight / (height ** 2)

def main():
    @validate_input
    def berat_badan_ideal(height, weight):
        bmi = calculate_bmi(height, weight)
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 24.9 <= bmi < 29.9:
            return "Gemuk"
        else:
            return "Obesitas"

    try:
        tinggi_badan = float(input("Masukkan tinggi badan (dalam meter): "))
        berat_badan = float(input("Masukkan berat badan (dalam kilogram): "))

        hasil = berat_badan_ideal(tinggi_badan, berat_badan)
        print("Berat badan Anda termasuk kategori:", hasil)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
