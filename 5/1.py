# 1.Encapsulation

class Car:
    def __init__(self,color,speed,model):
        self.color = color
        self.speed = speed
        self.model = model


    def drive(self):
        print(f"Mashinaning rangi: {self.color}\nTezkigi {self.speed} km\h\nModeli: {self.model}")


car1 = Car('red',20,'BMW')
car1.drive()