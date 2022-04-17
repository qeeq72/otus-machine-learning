from vehicle import Vehicle
from exceptions import CargoOverloadError


class Plane(Vehicle):
    def __init__(self, max_cargo, *args):
        super().__init__(*args)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, additional_cargo):
        cargo_total = self.cargo + additional_cargo
        if self.max_cargo >= cargo_total:
            self.cargo = cargo_total
        else:
            raise CargoOverloadError(cargo_total, self.max_cargo)

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before


if __name__ == "__main__":
    an225 = Plane(150000, False, 285000)
    an225.load_cargo(1000)
    an225.remove_all_cargo()
    print(vars(an225))