# Grades
# If Statements to check if a student at random has passed or failed an exam

import random

grade = random.randint(0, 100)

if grade > 55:
  print("You passed!")
else:
  print("You failed!")
