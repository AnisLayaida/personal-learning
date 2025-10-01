# Guess the Number
# For a While Loop to break, the condition inside must be met, otherwise it will run FOREVER

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  tries = tries + 1

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')