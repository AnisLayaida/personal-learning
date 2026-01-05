# These are the different modes
# 'r' is for reading a file
# 'w' is for writing to a file (this will overwrite the current file)
# 'a' is for writing from the end of a file

# write() method is used to write data to a file
file = open('test.txt', 'r')

file.write('text')

file.write('This is a line.\n')
file.write('This is the next line.\n')

lines = ['This is a line.\n', 'This is the next line.\n']
file.writeline(lines) # writeline() method lets you read the entire content of a file

# Reading Files allow you to read from files
# the .read() method lets to read content of the entire file

content = file.read()

print(content)

# .readlines() method lets you read all lines in a list

line = file.readlines()

for line in lines:
    print(line, end="")

# Closing files

file = open('filename.txt', 'r')
file.close()

# Task: Make a playlist and send it to a .txt file

def write_liked_songs_to_file(filename, liked_songs):
    with open(filename, 'w') as file:
        for song, artist in liked_songs.items():
            file.write(f"{song} - {artist}\n")

liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
}

write_liked_songs_to_file("playlist.txt", liked_songs)
