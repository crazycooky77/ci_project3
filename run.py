from random import randrange

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def roll_dice(dice_nr):
	'''
	Function for random number output to simulate dice rolls
	'''
	return(randrange(1, dice_nr + 1))

def character_selection():
	'''
	Function for the user to select their character
	'''
	# Provide character details to user
	print('''
You can choose between 4 characters:
1) A Witch with powerful magical abilities
2) A Druid who can transform ino a jaguar
3) A mischievous Pixie who attacks with pixie dust
4) A Nymph, who is a friend to, and will be aided by, trees
		''')

	while True:

		# Get user input for character selection
		selection = input('Type in the number or character type to make your selection: ')

		# If valid, enter character selection into a variable
		if selection == '1' or selection.capitalize() == 'Witch':
			character = 'Witch'
		elif selection == '2' or selection.capitalize() == 'Druid':
			character = 'Druid'
		elif selection == '3' or selection.capitalize() == 'Pixie':
			character = 'Pixie'
		elif selection == '4' or selection.capitalize() == 'Nymph':
			character = 'Nymph'

		# Print the selected character to the user if valid
		try:
			print(f'You selected {character}')
			return character
			break
		# Repeat the loop if invalid, to get a valid selection
		except UnboundLocalError:
			print(f'\nYou entered {selection}. Please type 1 or Witch, 2 or Druid, 3 or Pixie, 4 or Nymph')
			continue

# Start the game
print('Welcome to Woodlands and Witches! Let\'s begin our game')
character_selection()