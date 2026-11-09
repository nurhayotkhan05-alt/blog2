class Bird:
    def holati(self):
        print("Qush uchadi")

class Gipard:
    def holati(self):
        print("meaw meaw")

class Dog:
    def holati(self):
        print("Wow wow")

animals = [Bird(),Gipard(),Dog()]

for animal in animals:
    animal.holati()