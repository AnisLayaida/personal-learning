# The Cyclone
# Logical Operators are statements used to determine what output needs to be printed based on the input

print("How tall are you in cm?")
users_height = int(input())
print("How many credits do you have?")
users_credit = int(input())

if users_height >= 137 and users_credit >= 10:
  print("Enjoy the ride!")
elif users_height < 137 and users_credit >= 10:
  print("Sorry, you are not tall enough to ride.")
elif users_height >= 137 and users_credit <10:
  print("Sorry, you do not enough credits to enter the ride")
elif users_height < 137 and users_credit < 10:
  print("You have not met the requirements for either.")