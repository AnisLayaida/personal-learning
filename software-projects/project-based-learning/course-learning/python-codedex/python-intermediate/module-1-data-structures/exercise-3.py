# Dictionaries
# Dictionaries are ordered collections that allow us to store and access data using key:value pairs

# single line
# dictionary = {key1: value1, key2: value2, key3: value3}

# multi-line
# dictionary = {
#  key1: value1,
#  key2: value2,
#  key3: value3
# }

laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023
}

# To print, do the following:
print(laptop['brand'])
# Output: Apple

student_info = {
    'name': 'Anis',
    'age': 21,
    'ethnicity': "Algerian",
    'degree': "Digital and Technology Solutions Bsc",
    'height': 1.75,
}

print('Name:', student_info['name'])

# Modifying student Info

student_info['age'] = 22
print('The updated age', student_info['age'])

# Dictionary methods
print('Keys:', student_info.keys())
print('Values:', student_info.values())
print('Items:', student_info.items())

# Data Structure: Famous Foods from different ethnicities

famous_foods = {
    'Algerian': 'Couscous',
    'Ethiopian': 'Injera',
    'Kenyan': 'Ugali',
    'Sudanese': 'Kashkouli',
    'Eritrean': 'Telwa',
    'Somali': 'Bisbe',
    'Indian': 'Chapati',
    'Nigerian': 'Jollof Rice',
    'Ghanaian': 'Jollof Rice'
}

print('Ghanaian', famous_foods['Ghanaian'])

famous_foods['Algerian'] = 'Tagine'
print('The updated Algeria Food', famous_foods['Algerian'])

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
 