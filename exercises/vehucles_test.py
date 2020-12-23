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

import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        pass

    def test_car_not_enough_fuel(self):
        car = Car(100, 3)
        car.drive(40)

        self.assertEqual(car.fuel_quantity, 100)
    def test_car_enough_fuel(self):
        car_1 = Car(40, 3)
        car_1.drive(10)
        self.assertEqual(car_1.fuel_quantity,1)

    def test_refuel_car(self):
        car = Car(40, 3)
        car.refuel(40)

        self.assertEqual(car.fuel_quantity, 80)

    def test_truck_not_enough_fuel(self):
        truck = Truck(100, 3)
        truck.drive(40)

        self.assertEqual(truck.fuel_quantity, 100)

    def test_truck_has_enough_fuel(self):
        truck = Truck(50, 3)
        truck.drive(10)

        self.assertEqual(truck.fuel_quantity, 4)

    def test_truck_refuel(self):
        truck = Truck(30, 3)
        truck.refuel(40)

        self.assertEqual(truck.fuel_quantity, 68)

if __name__ == "__main__":
    unittest.main()