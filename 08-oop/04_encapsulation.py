"""

Problem 04: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

"""


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def full_name(self):
        return f"{self.__brand}: {self.__model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = ElectricCar("Tesla", "Model S", "80KWH")
print(my_car.get_brand())
print(my_car.set_brand("New brand"))
print(my_car.get_brand())
