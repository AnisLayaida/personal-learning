class Human:
    def __init__(self, name: str, age: int, gender: bool) -> None:
        self.name = name
        self._age = age
        self.__gender = gender

    def __str__(self) -> str:
        return (f"Is this information correct about yourself? ->"
                f" Your name is {self.name}, "
                f"your age is {self._age} and "
                f"you're a male, true? {self.__gender}")

    def get_name(self)-> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int):
        self._age = age

    def get_gender(self) -> bool:
        return self.__gender

    def set_gender(self, gender: bool):
        self.__gender = gender

Anis = Human("Anis", 20, True)

print(Anis)
