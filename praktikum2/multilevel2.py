#contoh 3
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} speaks")
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan}")
class Garuda(Bird):
    def __init__(self, name, wingspan, color):
        super().__init__(name, wingspan)
        self.color = color
    def speak(self):
        print(f"{self.name} is a {self.color} garuda that talks")
garuda = Garuda("Manuk", 66, "pink")
garuda.speak() 
garuda.fly() 