"""

Problem 08: Use a property decorator in the Car class to make the model attribute read-only.

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


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Tata", "Safari")
# print(my_car.general_desc())
# print(Car.general_desc())

print(my_car.model)
print(my_car.get_model())
