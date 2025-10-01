class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age

class Male(Human):
    def __init__(self, name: str, age: int, eye_colour: str, facial_hair: bool):
        super().__init__(name, age)
        self.eyeColour = eye_colour
        self.facialHair = facial_hair

    def __str__(self) -> str:
        return (f"Name: {self.name}, Age: {self._age}, "
                f"Eye Colour: {self.eyeColour}, "
                f"Facial Hair: {'Yes' if self.facialHair else 'No'}")


John = Male("Anis", 20, "Green", True)

print(John)