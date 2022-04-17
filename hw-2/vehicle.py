from abc import ABC
from exceptions import LowFuelError, NotEnoughFuelError


class Vehicle(ABC):
    def __init__(self, is_started, weight=0, fuel_level=0, fuel_consumption=0):
        self.__is_started = is_started
        self.weight = weight
        self.fuel_level = fuel_level
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.__is_started is not True:
            if self.fuel_level > 0:
                self.__is_started = True
            else:
                raise LowFuelError(self.fuel_level)

    def stop(self):
        self.__is_started = False

    def move(self, distance):
        self.start()
        fuel_per_move = (distance / 100) * self.fuel_consumption
        if self.fuel_level >= fuel_per_move:
            self.fuel_level = self.fuel_level - fuel_per_move
        else:
            raise NotEnoughFuelError(self.fuel_level, distance)


if __name__ == "__main__":
    v = Vehicle(False, 100, 50, 5)
    v.start()
    v.move(1000)
    v.stop()