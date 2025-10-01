# Pokedex
# Create a Pokemon class and then create objects that are real pokemon!

class Pokemon:
    def __init__(self, entry, name, type, description, is_caught):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        return f"{self.name} {self.name}"

    def display_details(self):
        return f"""Entry Number: {self.entry}
Name: {self.name}
Type: {self.type}
Description: {self.description}
                 """

    def caught(self):
        if self.is_caught == True:
            return "Pokemon has been caught!"
        else:
            return "Pokemon still on the lookout!"

pikachu = Pokemon(35, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", False)
charizard = Pokemon(78, "Charizard", "Fire", "A fire dragon with the ability to fire spin, air slash and use his amazing framethrower!", True)
bulbasaur = Pokemon(45, "Bulbasaur", "Poison", "Overgrows and boosts grass when HP is low!", False)

print(pikachu.speak())
print(charizard.speak())
print(bulbasaur.speak())

print(pikachu.display_details())
print(charizard.display_details())
print(bulbasaur.display_details())

print(pikachu.caught())
print(charizard.caught())
print(bulbasaur.caught())