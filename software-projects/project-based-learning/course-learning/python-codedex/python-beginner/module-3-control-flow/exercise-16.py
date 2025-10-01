# Sorting Hat
# Use all the Control flow exercises to create a sorting hat for the Hogwarts School of Witchcraft and Wizardry!

print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
question_1 = int(input())

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
question_2 = int(input())

print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
question_3 = int(input())

team_gryffindor = 0
team_ravenclaw = 0
team_hufflepuff = 0
team_slytherin = 0

if question_1 == 1:
  team_gryffindor +=1
if question_1 == 1:
  team_ravenclaw +=1
elif question_1 == 2:
  team_hufflepuff +=1
elif question_1 == 2:
  team_slytherin +=1

if question_2 ==1:
  team_hufflepuff +=2
elif question_2 ==2:
  team_slytherin +=2
elif question_2 ==3:
  team_ravenclaw +=2
elif question_2 ==4:
  team_gryffindor +=2

if question_3 ==1:
  team_slytherin +=4
elif question_3 ==2:
  team_hufflepuff +=4
elif question_3 ==3:
  team_ravenclaw +=4
elif question_3 ==4:
  team_gryffindor +=4

print("These are the results for all the houses!")
print("🦁 Gryffindor:")
print(team_gryffindor)
print("🦅 Ravenclaw:")
print(team_ravenclaw)
print("🦡 Hufflepuff:")
print(team_hufflepuff)
print("🐍 Slytherin:")
print(team_slytherin)