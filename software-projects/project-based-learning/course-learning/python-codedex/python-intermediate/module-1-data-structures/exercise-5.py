# Post Game Stats
# Recap

# Tuples are ordered sequences that cannot be changed
# Dictionaries are ordered sequences in key:value pairs
# Sets are unordered sequences of unique items

# Tuple
teams = ('TeamA', 'TeamB')

# Dictionary
basketball_player = {'name': 'LeBron James', 'team': 'Los Angeles Lakers'}

# Set
soccer_positions = {'Forward', 'Midfielder', 'Defender', 'Goalkeeper'}

# Task for today: Imagine you have a dataset with information about your favourite sports team
# Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name', 'position', and 'jersey number'.
# Print out a list of all player positions in the dataset.
# Choose a player and update their game statistics in the dataset.
# Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.

players = ["Saka", "Ronaldo", "Messi"]
positions = ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']

players[0] = {
    'name': 'Bukayo Saka',
    'position': positions[0],
    'jersey_number': 7,
    'goals': 68,
    'assists': 33,
    'average G/A': 68/33
}

players[1] = {
    'name': 'Cristiano Ronaldo',
    'position': positions[0],
    'jersey_number': 7,
    'goals': 950,
    'assists': 287,
    'average G/A': 950/287
}

players[2] = {
    'name': 'Lionel Messi',
    'position': positions[1],
    'jersey_number': 10,
    'goals': 895,
    'assists': 401,
    'average G/A': 895/401
}

print(players)