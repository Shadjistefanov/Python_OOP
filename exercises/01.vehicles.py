from abc import ABC, abstractmethod


class Vehicle(ABC):
    fuel_quantity: int
    fuel_consumption: int

    def __init__(self, fuel, consumption):
        self.fuel_quantity = fuel
        self.fuel_consumption = consumption

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._CONSUMPTION_PER_KM)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed

    @property
    @abstractmethod
    def _CONSUMPTION_PER_KM(self):
        ...

class Car(Vehicle):
    _CONSUMPTION_PER_KM = 0.9
    def refuel(self, fuel):
        super().refuel(fuel)

    # def drive(self, distance):
    #     super().drive(distance)

class Truck(Vehicle):
    _CONSUMPTION_PER_KM = 1.6
    def refuel(self, fuel):
        super().refuel(fuel * 0.95)

    # def drive(self, distance):
    #     super().drive(distance)

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

