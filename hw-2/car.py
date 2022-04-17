from vehicle import Vehicle
from engine import Engine
from exceptions import InvalidEngineError


class Car(Vehicle):
    def __init__(self, *args):
        super().__init__(*args)
        self.engine = None

    def set_engine(self, engine):
        engine_datatype = type(engine)
        if engine_datatype != Engine:
            raise InvalidEngineError(engine_datatype)

        self.engine = engine


if __name__ == "__main__":
    nissan_murano = Car(True, 1800, 70, 12)
    vq35de = Engine(3.5, 6)
    nissan_murano.set_engine(vq35de)
    print(vars(nissan_murano))
