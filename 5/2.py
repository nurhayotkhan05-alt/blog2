# Inhertance

class Car:
    def __init__(self,model,speed):
        self.model = model
        self.speed = speed

    def drive(self):
        print(f"Mashinaning nomi: {self.model}\n Tezligi: {self.speed} km\h\n\n")

car1 = Car('BMW',20)
car1.drive()

class Super_Car(Car):
    def __init__(self,model,speed,color):
        super().__init__(model,speed)
        self.color = color

    def superb_drive(self):
        print("Mashinaning nomi",self.model)
        print(f"Mashinaning tezligi: {self.speed} km\h")
        print(f"Masinaning rangi: {self.color}")

car2 = Super_Car("Cobolt",30,'ko\'k')
car2.drive()
car2.superb_drive()