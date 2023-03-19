#Jafar Maulana Ihsan
#210511044
#R4 - D

class celcius:

    def __init__(self,celcius):
        self.celcius=celcius

    def fahrenhiet(self):
        return (self.celcius * 9/5) + 32

    def kelvin(self):
        return (self.celcius + 273.15)

    def reimur(self):
        return (self.celcius * 4/5)

celciusE = celcius(50)

print(f"celcius ke fahrenhiet : {celciusE.fahrenhiet()}")
print(f"celcius ke kelvin : {celciusE.kelvin()}")
print(f"celcius ke reimur : {celciusE.reimur()}")