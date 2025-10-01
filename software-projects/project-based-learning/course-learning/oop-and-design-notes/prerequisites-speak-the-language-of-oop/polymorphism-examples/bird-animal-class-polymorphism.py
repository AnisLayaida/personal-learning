class Animal:
    def __init__(self, breed: str, amount_of_legs: int, weight: int):
        self.breed = breed
        self._amountOfLegs = amount_of_legs
        self.__weight = weight

    def get_weight(self) -> int:
        return self.__weight

    def noise(self):
        return "An animal noise"

    def __str__(self) -> str:
        return f"{self.breed}, {self._amountOfLegs}, {self.get_weight()}kg"

class Bird(Animal):
    def __init__(self, breed: str, amount_of_legs: int, weight: int, wild_bird: bool, carnivore: bool):
        super().__init__(breed, amount_of_legs, weight)
        self.wildBird = wild_bird
        self.carnivore = carnivore

    def noise(self):
        return "Tweet!"

    def __str__(self) -> str:
        return f"{self.breed}, {self._amountOfLegs},{self.get_weight()}kg,{self.wildBird},{self.carnivore}"

Mammal = Animal("Cat", 4, 108)
CanaryBird = Bird("Canary", 2, 1, True, False)

print(Mammal)
print(CanaryBird)
print(Mammal.noise())
print(CanaryBird.noise())