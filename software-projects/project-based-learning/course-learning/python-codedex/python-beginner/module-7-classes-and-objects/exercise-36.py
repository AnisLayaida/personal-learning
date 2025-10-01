# Favourite Cities
# __init__() method helps us construct object with unique attributes

class City:
    def __init__(self, name, country, population, landmarks, mayor, transport, capital):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.mayor = mayor
        self.transport = transport
        self.capital = capital

london = City("London", "UK", 10000000, "Big Ben", "Sadiq Khan", "TFL", True)
nyc = City("New York", "USA", 8480000, "Statue of Liberty", "Zohran Mamdani", "NYC Underground", False)

print(vars(london))
print(vars(nyc))

