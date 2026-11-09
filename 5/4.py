from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass


class Dog:
    def sound(self):
        print("Wow wow")

class Cat(Animal):
    def sound(self):
        print("Miyav,Miyav")


