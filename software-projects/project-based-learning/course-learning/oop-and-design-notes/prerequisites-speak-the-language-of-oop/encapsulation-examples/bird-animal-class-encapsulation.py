class Animal:
    def __init__(self, breed: str, amount_of_legs: int, weight: int):
        self.breed = breed
        self._amountOfLegs = amount_of_legs
        self.__weight = weight

    def get_amount_of_legs(self) -> int:
        return self._amountOfLegs

    def set_amount_of_legs(self, amount_of_legs: int):
        self._amountOfLegs = amount_of_legs

    def get_weight(self) -> int:
        return self.__weight

    def set_weight(self, weight: int):
        self.__weight = weight

    def noise(self):
        return "An animal noise"

    def __str__(self) -> str:
        return f"{self.breed}, {self._amountOfLegs}, {self.get_weight()}kg"

class Bird(Animal):
    def __init__(self, breed: str, amount_of_legs: int, weight: int, dark_colour: bool, wild_bird: bool, carnivore: bool):
        super().__init__(breed, amount_of_legs, weight)
        self.darkColour = dark_colour
        self._wildBird = wild_bird
        self.__carnivore = carnivore

    def get_wild_bird(self) -> bool:
        return self._wildBird

    def set_wild_bird(self, wild_bird: bool):
        self._wildBird = wild_bird

    def get_carnivore(self) -> bool:
        return self.__carnivore

    def set_carnivore(self, carnivore: bool):
        self.__carnivore = carnivore

    def noise(self):
        return "Tweet!"

    def __str__(self) -> str:
        return f"{self.breed}, {self.get_amount_of_legs()}, {self.get_weight()}kg, {self.get_wild_bird()}, {self.get_carnivore()}"

Mammal = Animal("Cat", 4, 108)
CanaryBird = Bird("Canary", 2, 1, True, False, False)

print(Mammal)
print(CanaryBird)
print(Mammal.noise())
print(CanaryBird.noise())