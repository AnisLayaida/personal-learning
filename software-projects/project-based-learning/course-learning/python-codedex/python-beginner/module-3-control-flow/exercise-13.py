# pH Levels
# Using Relational operators (==, !=, >, etc) on top of the if statement

ph_level = int(input())

if ph_level > 7:
  print("Basic Level")
elif ph_level == 7:
  print("Neutral")
elif ph_level < 7:
  print("Acidic")
