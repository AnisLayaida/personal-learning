# Slot Machine
# Look further into Modules and what they do in python

import random
import math

symbols = ['🍒','🍇','🍉','7️⃣ ']

results = random.choices(symbols, k=3)

output = print(" | ".join(results))

if results.count("7️⃣") == 3:
  print("Jackpot! 💰")
elif results.count("🍉") == 3:
  print("Win!")
elif results.count("🍇") == 3:
  print("Win!")
elif results.count("🍒") == 3:
  print("Win!")
else:
  print("Keep on playing!")
