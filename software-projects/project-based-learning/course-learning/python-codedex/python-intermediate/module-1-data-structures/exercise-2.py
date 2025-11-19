# Tuples are ordered collections that cannot be changed after creation
# They are immutable, meaning their value cannot change
# Lists use [], Tuples can use () or nothing (as long as they have a comma) and can have all sorts of data types

my_dna = ('GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT')
print(my_dna[3]) # Will print the 4th value -> TAA

full_name = ('Anis', 'Layaida')
first_name = full_name[0]
last_name = full_name[1]
print(first_name, last_name) # Will print Anis Layaida

# Combining Tuples

name_1 = 'Khabib',
name_2 = 'Abdulmanapovich',
name_3 = 'Nurmagovedov',
full_names = name_1 + name_2 + name_3
print(f"Do you prefer {name_1} {name_3} or {full_names}?")

# Exercise 2: Create a Tuple for the city you are in, 3 tuples for the name of friends and their locations

locations = ["Birmingham", "London", "Paris"]
friend_1 = 'Adam',
friend_2 = 'Bob',
friend_3 = 'Charlie'

print(f"{friend_1} is in {locations[0]}, {friend_2} lives in {locations[2]} and {friend_3} lives near {locations[1]}")

 