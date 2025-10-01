# Bucket List
# Task is to create a list to do, remove an existing index within the list and then print a specific index from the list

things_to_do = [
  '🚀 Create the dopest learn to code platform ever.',
  '⛰️ Hike the Pacific Crest Trail.',
  '🏡 Build an A-frame house and raise some goats.',
  '🌏 Live somewhere in Asia for a year.',
  '🎸 Release an album.',
  '📝 Write a book.',
  '🏆 Reach 100k subscribers on YouTube.',
  '🚐 Road trip with the fam.',
  '🍳 Open a cozy diner upstate.',
  '👴🏻 Grow old with no regrets.'
]

things_to_do.remove('🏡 Build an A-frame house and raise some goats.')

for i in things_to_do:
  print(i)