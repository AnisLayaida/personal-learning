# Solar System
# Different ways of importing objects from modules

from math import pi
from random import choice as ch

planets = ['Mercury','Venus','Earth','Mars','Saturn']

random_planet = ch(planets)

if random_planet == planets[0]:
  r = 2440
elif random_planet == planets[1]:
  r = 6052
elif random_planet == planets[2]:
  r = 6371
elif random_planet == planets[3]:
  r = 3900
elif random_planet == planets[4]:
  r = 58232
else:
  print("Oops, an error occured!")

area = 4*pi*r**2

print(f"The planet {random_planet} has the area {round(area)}")