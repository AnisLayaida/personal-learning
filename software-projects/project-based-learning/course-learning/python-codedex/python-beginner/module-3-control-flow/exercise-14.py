# Magic 8 Ball
# Using the Random Module in python along with if and elif statements to create a magic 8 ball

import random

num = random.randint(1, 9)

print("Enter any question you would like the answer to :)")
question = input()

if num == 1:
  print("Yes - definitely.")
elif num == 2:
  print("It is decidedly so.")
elif num == 3:
  print("Without a doubt")
elif num == 4:
  print("Reply hazy, try again")
elif num == 5:
  print("Ask again later")
elif num == 6:
  print("Better not tell you now.")
elif num == 7:
  print("My Sources say no.")
elif num == 8:
  print("Outlook not so good.")
elif num == 9:
  print("Very Doubtful")