from random import randrange
import time


# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def roll_dice(roll_request, dice_nr):
	"""
	Function for random number output to simulate dice rolls
	"""
	input(f'''
{roll_request}
Enter any text, or just press the "Enter" key, to roll the die.\n''')
	die_roll = randrange(1, dice_nr + 1)
	print(f'You rolled {die_roll}.')
	return die_roll


def game_selections(input_req, wrong_input, *choices):
	"""
	Functions that let the user make custom choices in the game
	"""
	while True:

		# Get user input for game selection
		game_sel = input(input_req)

		# If valid, enter selection into a variable
		if game_sel.capitalize() in choices:
			selection = game_sel.capitalize()
		elif 0 <= int(game_sel) <= len(choices):
			selection = choices[int(game_sel) - 1]

		# Print the selection to the user if valid
		try:
			print(f'You selected {selection}')
			return selection
		# Repeat the loop if invalid, to get a valid selection
		except UnboundLocalError:
			print(f'\nYou entered {game_sel}. ' + wrong_input)
			continue


def gameplay():
	"""
	Function that runs the full game
	"""
	print('Welcome to Woodlands and Witches! Let\'s begin our game')
	time.sleep(1)

	# Character selection
	print('''
You can choose between 4 characters:
1) A Witch with powerful magical abilities
2) A Druid who can transform into a jaguar
3) A mischievous Pixie who attacks with pixie dust
4) A Nymph, who is a friend to, and will be aided by, trees
		''')
	char_sel = 'Type in the number or character type to make your selection: '
	char_invalid = 'Please type 1 or Witch, 2 or Druid, 3 or Pixie, 4 or Nymph'
	characters = ['Witch', 'Druid', 'Pixie', 'Nymph']
	character = game_selections(char_sel, char_invalid, *characters)

	# Pause before continuing the game
	time.sleep(1)
	print('''
You wake up in the middle of a dark forest.
There are 3 paths ahead of you.
1) One path leads to a Cave.
2) One leads to a Clearing.
3) The last path leads to a River.
What do you choose?
		''')

	# First story choice for the user
	first_req = 'Type in the number or location to make your selection: '
	first_invalid = 'Please type 1 or Cave, 2 or Clearing, 3 or River'
	first_choices = ['Cave', 'Clearing', 'River']
	game_selections(first_req, first_invalid, *first_choices)

	# Pause before continuing the game
	time.sleep(1)
	first_roll = 'Roll the dice to determine what happens when you arrive at your destination.'
	# User rolls die
	first_die = roll_dice(first_roll, 6)
	time.sleep(1)
	# Outcome of first die roll
	if (first_die % 2) == 0:
		print('''
A giant panther appears, goes up to you,
and nudges your hand with it's head.
It wants to make friends!
		''')
	else:
		print('''
A giant panther appears, looking at you menacingly...
What will you do? Roll the dice!
		''')


# Start the game
gameplay()
