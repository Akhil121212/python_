#oops
class car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"    

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "petrol or diesel"    

class ElectricCar(car):
    def __init__(self, brand,model,battery_size):
        super().__init__(brand,model) 
        self.battery_size = battery_size

    def fuel_type(self):

my_tesla = ElectricCar("tesla","model S","85KWH")
print(my_tesla.full_name())
print(my_tesla.get_brand())





my_car = car("tata","safari")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

int(10)



