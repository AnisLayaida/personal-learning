# Coin Flip
# Control Flow is the order your program runs things at runtime:
# It controls if the code does the right thing, does it work extra and can humans follow the path?
# Think of your code as like a flowchart essentially

import random

num = random.randint(0, 1)

if num > 0.5:
  print("Heads")
else:
  print("Tails")