class Car:
    def __init__(self, max_speed: int, colour: str, engine_size: float):
        self.maxSpeed = max_speed  # Public (+)
        self._colour = colour  # Protected (#)
        self.__engineSize = engine_size  # Private (-)

    def __str__(self) -> str:
        return (f"Here is some information about your car "
                f"The maximum speed (mph): {self.maxSpeed} -> "
                f"The colour of the car: {self._colour} -> "
                f"The engine size of the colour (in litres): {self.__engineSize}")

    def get_max_speed(self) -> int:
        return self.maxSpeed

    def set_max_speed(self, max_speed: int) -> None:
        self.maxSpeed = max_speed

    def get_colour(self) -> str:
        return self._colour

    def set_colour(self, colour: str) -> None:
        self._colour = colour

    def get_engine_size(self) -> float:
        return self.__engineSize

    def set_engine_size(self, engine_size: float) -> None:
        self.__engineSize = engine_size

BMW = Car(130, "Black", 4.8)

print(BMW)