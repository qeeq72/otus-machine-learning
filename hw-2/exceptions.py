class LowFuelError(Exception):
    def __init__(self, fuel=0):
        self.fuel_level = fuel
        self.msg = "Fuel level is low"
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.fuel} -> {self.msg}'


class NotEnoughFuelError(Exception):
    def __init__(self, fuel=0, distance=0):
        self.fuel = fuel
        self.distance = distance
        self.msg = "Fuel level is not enough to move"
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.fuel} -> {self.msg} {self.distance} km'


class CargoOverloadError(Exception):
    def __init__(self, cargo=0, max_cargo=0):
        self.max_cargo = max_cargo
        self.cargo = cargo
        self.msg = "Cargo is overloaded by"
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.cargo} -> {self.msg} {self.cargo - self.max_cargo}'


class InvalidEngineError(Exception):
    def __init__(self, engine_datatype):
        self.engine_datatype = engine_datatype
        self.msg = "Invalid engine datatype"
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.engine_datatype} -> {self.msg}'