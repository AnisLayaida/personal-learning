# Fruit Cart

# Sets are collections of unique items with no duplicates
# They are an unordered collection of distinct elements
# Each item in a set must be unique

# Sets do not have an inherited order, making them perfect for scenarios where the sequence of the element is not important

# When are sets useful? Working with a database of user profiles, each with a unique ID.

# set_example = {val1, val2, val3}

fruits = {'🍎 apple', '🍌 banana', '🍊 orange'}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets = Combines two or more sets and returns the new larger set
# union_result = set1.union(set2) # {1, 2, 3, 4, 5, 6}

# Intersection of sets = Returns all values that overlap in two or more sets
# intersection_result = set1.intersection(set2) # {3, 4}

# Difference of sets = Returns a set of items found only in the calling set
# difference_result = set1.difference(set2) # {1, 2}

my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set) # Output: {1, 3, 4}

# Output:
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}


# Task: Create two sets representing your favourite fruits and your best friends fruits!
# Print the union of the two sets as well as the intersection
# Also try see the difference between the two sets are

anis_5_favourite_fruits = {'Apple', 'Banana', 'Pineapple', 'Pomegranate', 'Orange'}
grandma_5_favourite_fruits = {'Banana', 'Mango', 'Pomegranate', 'Orange', 'Watermelon'}

union_result = anis_5_favourite_fruits.union(grandma_5_favourite_fruits)
intersection_result = anis_5_favourite_fruits.intersection(grandma_5_favourite_fruits)
difference_result = anis_5_favourite_fruits.difference(grandma_5_favourite_fruits)

print(union_result)
print(intersection_result)
print(difference_result)