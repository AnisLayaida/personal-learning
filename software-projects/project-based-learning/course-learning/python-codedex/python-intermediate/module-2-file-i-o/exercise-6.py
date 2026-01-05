# File Handling

# File input/output (I/O) handing lets us interact with external files for various purposes, such as:
# Saving info to a file by writing to it
# Reading from a file to use its info
# Maintaining computor file systems

# open() method is your gateway to handle files in python
# It can create (if it doesnt exist) or open (if it exists)

# file = open(file_name, mode)
file = open('example.txt', 'w') # Opens example file for writing

file.write("Hello World!!") # The write() method allows you to write in the file

# Intructions: Use the open() method to create a new diary and write your secrets inside!

file = open('diary.txt', 'w')
file.write("I'm currently learning python! Im also very hungry lol")