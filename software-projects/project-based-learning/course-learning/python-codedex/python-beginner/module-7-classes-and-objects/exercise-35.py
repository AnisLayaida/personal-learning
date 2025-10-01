# Bob's Burgers
# Create a Restaurant class and multiple objects from that class

class Restaurant:
  name = ""
  type = ""
  rating = 0.0
  halal = False

bobs_burgers = Restaurant()
bobs_burgers.name = "Bobs Burgers"
bobs_burgers.type = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.halal = False

wingstop = Restaurant()
wingstop.name = "Wingstop"
wingstop.type = "Chicken Shop"
wingstop.rating = 4.8
wingstop.halal = True

macdonalds = Restaurant()
macdonalds.name = "MacDonalds"
macdonalds.type = "Fast Food Restaurant"
macdonalds.ratings = 3.0
macdonalds.halal = False

print(vars(bobs_burgers))
print(vars(wingstop))
print(vars(macdonalds))