class Animal:
    def __init__(self, breed: str, amount_of_legs: int, weight: int):
        self.breed = breed
        self._amountOfLegs = amount_of_legs
        self.__weight = weight

    def get_weight(self) -> int:
        return self.__weight


class Bird(Animal):
    def __init__(self, breed: str, amount_of_legs: int, weight: int, wild_bird: bool, carnivore: bool):
        super().__init__(breed, amount_of_legs, weight)
        self.wildBird = wild_bird
        self.carnivore = carnivore

    def __str__(self) -> str:
        return f"{self.breed}, Legs = {self._amountOfLegs}, Weight in kg: {self.get_weight()}kg, Wild Bird? {self.wildBird}, Carnivore? {self.carnivore}"

CanaryBird = Bird("Canary", 2, 1, True, False)

print(CanaryBird)