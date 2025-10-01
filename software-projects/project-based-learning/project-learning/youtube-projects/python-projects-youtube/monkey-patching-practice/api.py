from enum import Enum

class Builder(Enum):
    FENDER = "Fender"
    GIBSON = "Gibson"
    MARTIN = "Martin"
    YAMAHA = "Yamaha"
    OTHER = "Other"

class Type(Enum):
    ELECTRIC = "Electric"
    ACOUSTIC = "Acoustic"
    BASS = "Bass"

class Wood(Enum):
    MAPLE = "Maple"
    MAHOGANY = "Mahogany"
    ALDER = "Alder"
    ROSEWOOD = "Rosewood"
    SPRUCE = "Spruce"

class Guitar:
    def __init__(self, serial_number: str, price: float, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood):
        self.serialNumber = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.type = type
        self.backWood = back_wood
        self.topWood = top_wood

    def get_serial_number(self) -> str:
        return self.serialNumber

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: int):
        self.price = price

    def get_builder(self) -> Builder:
        return self.builder

    def get_model(self) -> str:
        return self.model

    def get_type(self) -> Type:
        return self.type

    def get_back_wood(self) -> Wood:
        return self.backWood

    def get_top_wood(self) -> Wood:
        return self.topWood

    def __str__(self) -> str:
        return (f"Guitar [Serial: {self.serialNumber}, Price: {self.price}, "
                f"Builder: {self.builder}, Model: {self.model}, Type: {self.type}, "
                f"Back Wood: {self.backWood}, Top Wood: {self.topWood}]")

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number: str, price: float, builder: Builder,
                   model: str, type: Type, back_wood: Wood, top_wood: Wood):
        guitar = Guitar(serial_number, price, builder, model, type, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number: str) -> Guitar:
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, search_guitar: Guitar) -> list:
        results = []
        for guitar in self.guitars:
            if (search_guitar.get_builder() == guitar.get_builder() and
                search_guitar.get_model().lower() == guitar.get_model().lower() and
                search_guitar.get_type() == guitar.get_type() and
                search_guitar.get_back_wood() == guitar.get_back_wood() and
                search_guitar.get_top_wood() == guitar.get_top_wood()):
                results.append(guitar)
        return results
