class Car:
    def __init__(self, max_speed: int, colour: str, engine_size: float):
        self.maxSpeed = max_speed  # Public (+)
        self._colour = colour  # Protected (#)
        self.__engineSize = engine_size  # Private (-)

    def get_engine_size(self) -> float:
        return self.__engineSize

    def display_info(self):
        return f"Displays information about the car, {self.maxSpeed}, {self._colour}, {self.get_engine_size()}"

class Coupe(Car):
    def __init__(self, max_speed: int, colour: str, engine_size: float, leather_seats: bool, number_of_doors: int, sports_mode: bool):
        super().__init__(max_speed, colour, engine_size)
        self.leatherSeats = leather_seats
        self.numberOfDoors = number_of_doors
        self.sportsMode = sports_mode

    def __str__(self) -> str:
        return (f"Coupe -> Max speed: {self.maxSpeed} mph, "
                f"Colour: {self._colour}, "
                f"Leather seats: {self.leatherSeats}, "
                f"Doors: {self.numberOfDoors}, "
                f"Sports mode: {'ON' if self.sportsMode else 'OFF'}")

    def display_info(self):
        return ("A Coupe is a type of car that’s usually:\n"
                "- 2 doors (classic definition).\n"
                "- Sporty and stylish.\n"
                "- Less practical than sedans or SUVs (smaller back seats + boot).\n"
                "- Focused more on performance and looks than family use.")


Audi = Car(160, "Blue", 6.6)
BMW = Coupe(155, "Red", 3.6, True, 4, True)


print(Audi.display_info())
print(BMW.display_info())