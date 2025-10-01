# Fizz Buzz
# Task is to replace any multiple of 3 with Fizz, any multiple of 5 with Buzz and any common multiple of both with FizzBuzz

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 1 == 0:
    print(i)