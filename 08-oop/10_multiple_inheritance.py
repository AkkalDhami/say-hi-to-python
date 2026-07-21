"""

Problem 10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

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

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

    def full_name(self):
        return f"{self.__brand}: {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_desc():
        return "Cars are means of transport."

    @property
    def model(self):
        return self.__model


class Battery:
    def battery_info(self):
        return "All Good! Battery"


class Engine:
    def engine_info(self):
        return "All Good! Engine"


class ElectricCar(Battery, Engine, Car):
    pass


new_car = ElectricCar("Test brand", "Model A")
print(new_car.battery_info())
print(new_car.engine_info())
