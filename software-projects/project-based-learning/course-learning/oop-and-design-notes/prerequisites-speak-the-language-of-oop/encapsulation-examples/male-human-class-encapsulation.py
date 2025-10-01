class Human:
    def __init__(self, name: str, age: int) -> None:
        self.height = height
        self._name = name
        self.__age = age

    def speak(self):
        return f"My Name is {self.name} and I am {self._age}"

    def __str__(self) -> str:
        return self.name


class Male(Human):
    def __init__(self, name: str, age: int, eye_colour: str, facial_hair: bool):
        super().__init__(name, age)
        self.eyeColour = eye_colour
        self.facialHair = facial_hair

    def speak(self):
        return (f"Name: {self.name}, Age: {self._age}, "
                f"Eye Colour: {self.eyeColour}, "
                f"Facial Hair: {'Yes' if self.facialHair else 'No'}")

    def __str__(self) -> str:
        return self.name


Mark = Human("Mark", 20)
John = Male("John", 24, "Green", True)

print(Mark)
print(John)

print(Mark.speak())
print(John.speak())