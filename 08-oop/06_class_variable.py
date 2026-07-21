"""

Problem 06: Add a class variable to Car that keeps track of the number of cars created.

"""


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def full_name(self):
        return f"{self.__brand}: {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = ElectricCar("Tesla", "Model S", "80KWH")
print(my_car.fuel_type())
print(Car.total_car)

safari = Car("Tata", "Safari")
print(safari.fuel_type())
print(safari.total_car)
