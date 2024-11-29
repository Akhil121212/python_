"""class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Akhil")        
print(s1.name)
del s1.name  #to delete any value
print(s1.name)"""

"""class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass__ = acc_pass

acc1 = Account("12345","abcdef")
print(acc1.acc_no)
print(acc1.__acc_pass__)        

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop(): 
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("pruls")

print(car1.start())
"""

#Multilevel inheritance

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Tata(Car):
    @staticmethod
    def __init__(self,brand):
        self.brand = brand

class Vehicle(Tata):
    def __init__(self,type):
        self.type = type     

car1 = Tata("petrol")
car1.start() 


