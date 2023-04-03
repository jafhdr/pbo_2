import pygame

class Animal:
    def __init__(self, name, sound_file):
        self.name = name
        self.sound_file = sound_file
    
    def speak(self):
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()

class Cat(Animal):
    def __init__(self):
        super().__init__('Cat', 'suara_kucing.mp3')

class Dog(Animal):
    def __init__(self):
        super().__init__('Dog', 'suara_anjing.mp3')

class Cow(Animal):
    def __init__(self):
        super().__init__('Cow', 'suara_sapi.mp3')

class Sheep(Animal):
    def __init__(self):
        super().__init__('Sheep', 'suara_kambing.mp3')

class Horse(Animal):
    def __init__(self):
        super().__init__('Horse', 'suara_kuda.mp3')

class Rooster(Animal):
    def __init__(self):
        super().__init__('Rooster', 'suara_ayam.mp3')

class Monkey(Animal):
    def __init__(self):
        super().__init__('Monkey', 'suara_monyet.mp3')

class Lion(Animal):
    def __init__(self):
        super().__init__('Lion', 'suara_singa.mp3')

class Bird(Animal):
    def __init__(self):
        super().__init__('Bird', 'suara_burung.mp3')

class Elephant(Animal):
    def __init__(self):
        super().__init__('Elephant', 'suara_gajah.mp3')

# inisialisasi pygame
pygame.init()

# membuat list dari objek-objek hewan
animals = [Cat(), Dog(), Cow(), Sheep(), Horse(), Rooster(), Monkey(), Lion(), Bird(), Elephant()]

# memutar suara dari setiap hewan dalam list
for animal in animals:
    print(animal.name)
    animal.speak()
    pygame.time.delay(1000)  # delay 1 detik sebelum memutar suara hewan berikutnya
    pygame.mixer.music.stop() # stop musik sebelum lanjut ke hewan berikutnya

# keluar dari program dan bersihkan pygame
pygame.quit()
