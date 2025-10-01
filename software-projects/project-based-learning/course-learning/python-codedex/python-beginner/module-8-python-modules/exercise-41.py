# Countdown
# You can create your own module, as a module is just a python file

import datetime
from bday_messages import random_message
import random

today = datetime.date.today()
next_birthday = datetime.date(2025, 9, 30)

days_away = (next_birthday - today).days

if days_away == 0:
    print("🎉 Happy Birthday!!! 🎉")
else:
    print(f"My next birthda is in {days_away} days!")
    print(random_message)
