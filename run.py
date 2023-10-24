from termcolor import colored, cprint
from random import randrange
import time


# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def roll_dice(roll_request, dice_nr):
	"""
	Function for random number output to simulate dice rolls
	"""
	input(f'''{roll_request}
Submit any text, or just press the "Enter" key, to roll the die.\n''')
	die_roll = randrange(1, dice_nr + 1)
	print(f'You rolled {die_roll}.\n')
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
		elif game_sel.isnumeric() and 0 <= int(game_sel) <= len(choices):
			selection = choices[int(game_sel) - 1]

		# Print the selection to the user if valid
		try:
			print(f'\nYou selected {selection}\n')
			return selection
		# Repeat the loop if invalid, to get a valid selection
		except UnboundLocalError:
			print(f'\nYou entered {game_sel}. ' + wrong_input)
			continue


def character_selection():
	"""
	Function that runs the first part of the story
	"""
	print('Welcome to Woodlands and Witches! Let\'s begin our game\n')
	# Pause before continuing the game
	time.sleep(3)

	# Character selection
	print('''You can choose between 4 characters:
1) A Witch with powerful magical abilities
2) A Druid who can transform into a jaguar
3) A mischievous Pixie who attacks with pixie dust
4) A Nymph, who is a friend to, and will be aided by, trees\n''')
	char_sel = 'Type in the number or character type to make your selection: '
	char_invalid = 'Please type 1 or Witch, 2 or Druid, 3 or Pixie, 4 or Nymph'
	characters = ['Witch', 'Druid', 'Pixie', 'Nymph']
	character = game_selections(char_sel, char_invalid, *characters)
	return character


def first_story_part(character):
	"""
	Function that runs the first part of the story
	"""
	print('''You wake up in the middle of a dark forest.
There are 3 paths ahead of you:
1) One path leads to a Cave.
2) One leads to a Clearing.
3) The last path leads to a River.
What do you choose?'\n''')

	# First story choice for the user
	first_req = 'Type in the number or location to make your selection: '
	first_invalid = 'Please type 1 or Cave, 2 or Clearing, 3 or River'
	first_choices = ['Cave', 'Clearing', 'River']
	game_selections(first_req, first_invalid, *first_choices)

	# Pause before continuing the game
	time.sleep(3)
	first_roll = 'Roll the dice to determine what happens when you arrive at your destination.'
	# User rolls die
	first_die = roll_dice(first_roll, 6)
	# Pause before continuing the game
	time.sleep(3)
	# Outcome of first die roll
	if (first_die % 2) == 0:
		# Pause before continuing the game
		time.sleep(3)
		# Lucky outcome for even numbers
		print('''A giant panther appears, goes up to you,
and nudges your hand with it's head.
It wants to make friends!\n''')
	else:
		# Unlucky outcome for odd numbers (first choice sub die roll)
		first_sub_roll = ('''A giant panther appears, looking at you menacingly...
What will you do? Roll the dice!\n''')
		# Unlucky outcome die roll
		first_sub_die = roll_dice(first_sub_roll, 20)
		if 1 <= first_sub_die <= 3:
			# Game over for die rolls 1 - 3
			print('''You try attacking the big cat, but you're too slow.
It swipes at you with a giant paw,
and everything turns black!\n''')
			# Pause before continuing the game
			time.sleep(3)
			print('You died... Game Over')
			quit()
		elif character == 'Witch':
			# Good Witch outcome for die rolls 4 - 20
			print('''You send a huge blast of arcane magic at the big cat and defeat it.
It agrees to help you on your quest.\n''')
		elif character == 'Pixie':
			# Good Pixie outcome for die rolls 4 - 20
			print('''You blow a huge cloud of pixie dust into the big cat's face.
It becomes charmed by you and your dust, and starts following you around.\n''')
		elif character == 'Nymph':
			# Good Nymph outcome for die rolls 4 - 20
			print('''You get your tree friends to help you.
They surround the big cat, who jumps up the branches and climbs the tree.
It falls asleep on the tree limbs, thanking you for the assistance.
It wants to repay the favour.\n''')
		elif character == 'Druid':
			# Good Druid outcome for die rolls 4 - 20
			print('''You transform into a jaguar and make friends with the big cat.
It joins you on your journey!\n''')


def second_story_part():
	"""
	Function that runs the second part of the story
	"""
	# Create variables for later use
	knock_lucky = None
	talk_crone = None
	barge_lucky = None
	ko_choice = None
	disagree = None

	# Pause before continuing the game
	time.sleep(5)
	print('''You continue on and see a little cabin
with smoke coming out of the chimney.
Do you Knock on the door, or Barge right in?\n''')

	# Second story choice for the user
	second_req = 'Type in the number or word to make your selection: '
	second_invalid = 'Please type 1 or Knock, 2 or Barge'
	second_choices = ['Knock', 'Barge']
	second_sel = game_selections(second_req, second_invalid, *second_choices)

	# Pause before continuing the game
	time.sleep(3)
	# Outcome of second user choice
	if second_sel == 'Barge':
		# User rolls die
		second_sub_roll = 'Roll the dice to see what awaits you inside the cabin.'
		second_sub_die = roll_dice(second_sub_roll, 20)

		if 1 <= second_sub_die <= 4:
			# Unlucky outcome
			print('You barge in and the old crone inside sends a blast of magic your way.')
			# Pause before continuing the game
			time.sleep(3)
			print('You died... Game Over')
			quit()
		else:
			# Lucky outcome
			print('''You barge in and tackle the old crone inside.
Do you Talk to her, or try to Knock her Out (KO)?\n''')
			barge_lucky = True

	elif second_sel == 'Knock':
		# User rolls die
		second_roll = 'Roll the dice to see who opens the door.'
		second_die = roll_dice(second_roll, 6)

		# Outcome of second die roll
		if (second_die % 2) != 0:
			# Lucky outcome
			print('An old crone opens the door and warmly welcomes you inside.')
			knock_lucky = True
		else:
			# Unlucky outcome
			print('''An old crone opens the door and looks at you suspiciously.
Do you 1) Talk to her or 2) try to Knock her Out (KO)?\n''')
			knock_lucky = False

	if (second_sel == 'Barge' and barge_lucky) or (second_sel == 'Knock' and knock_lucky is False):
		# Second choice sub choice outcome for the user
		second_sub_req = 'Type in the number or word to make your selection: '
		second_sub_invalid = 'Please type 1 or Talk, 2 or KO'
		second_sub_choices = ['Talk', 'KO']
		second_sub_sel = game_selections(second_sub_req, second_sub_invalid, *second_sub_choices)
		if second_sub_sel == 'Talk':
			talk_crone = True
		else:
			ko_choice = True

	if (
			(second_sel == 'Knock' and knock_lucky) or
			(knock_lucky is False and talk_crone) or
			(second_sel == 'Barge' and talk_crone)
		):
		# Third story choice for the user
		print('''You are the one the crone has seen in visions previously.
She wants to train you as her protege...
Do you agree?\n''')

		third_req = 'Type in 1 or Yes, 2 or No, to make your selection: '
		third_invalid = 'Please type 1 or Yes, 2 or No'
		third_choices = ['Yes', 'No']
		third_sel = game_selections(third_req, third_invalid, *third_choices)

		# Pause before continuing the game
		time.sleep(3)
		if third_sel == 'Yes':
			# First good ending option
			print('''You begin learning everything you can from your mentor.
Your story ends here... for now!''')
			quit()
		else:
			# Third story die roll for potential unlucky outcome
			print('The crone can\'t risk anyone else finding her cabin and attacks you.\n')
			disagree = True

		# Pause before continuing the game
		time.sleep(3)
		if disagree or ko_choice:
			third_roll = 'Roll the die to see if you\'re able to overpower the old crone!'
			# User rolls die
			third_die = roll_dice(third_roll, 20)

			# Pause before continuing the game
			time.sleep(3)
			# Outcome of third die roll
			if 16 <= third_die <= 20:
				# Game over for die rolls 16 - 20
				print('''You try to defend yourself, but the old crone overcomes you.
You're unable to stand against her might!\n''')
				# Pause before continuing the game
				time.sleep(3)
				print('You died... Game Over')
				quit()
			else:
				# Second good story ending option
				print('''You defeat the crone, take over her cabin,
and start looking through all of her ancient tomes.
You learn all you can of her magic and enchantments.
Your story ends here... for now!''')
				quit()


def gameplay():
	"""
	Function that runs the full game
	"""
	# Start the game
	character = character_selection()
	# Pause before continuing the game
	time.sleep(3)
	# First game options
	first_story_part(character)
	# Pause before continuing the game
	time.sleep(3)
	# Second set of game options
	second_story_part()


# Run the game
gameplay()
