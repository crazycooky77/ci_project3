from termcolor import colored
from random import randrange
import time
from storylines import *


# Custom exception for restart_game function
class NewGame(Exception):
    pass


def restart_game():
    """
    Function to enable the user to restart the game
    (for wins and losses)
    """
    restart = input('Play again? Y or N\n')
    if restart == 'Y' or restart == 'y':
        # Restart the game
        gameplay()
    elif restart == 'N' or restart == 'n':
        # Quit the game
        quit()
    else:
        # Ask for valid input
        print('Please enter "Y" or "N"')


def roll_dice(roll_request, dice_nr):
    """
    Function for random number output to simulate dice rolls
    """
    input(colored(f'''{roll_request}
Submit any text, or just press the "Enter" key, to roll the die.\n''',
                  'light_cyan'))
    die_roll = randrange(1, dice_nr + 1)
    print(colored(f'You rolled {die_roll}.\n', 'light_grey', attrs=['bold']))
    # Pause before continuing the game
    time.sleep(3)
    return die_roll


def game_selections(input_req, wrong_input, *choices):
    """
    Functions that let the user make custom choices in the game
    """
    while True:

        # Get user input for game selection
        game_sel = input(colored(input_req, 'light_cyan'))

        # If valid, enter selection into a variable
        if game_sel.capitalize() in choices:
            selection = game_sel.capitalize()
        elif game_sel.isnumeric() and 0 <= int(game_sel) <= len(choices):
            selection = choices[int(game_sel) - 1]

        # Print the selection to the user if valid
        try:
            print(colored(f'\nYou selected {selection}\n',
                          'light_grey', attrs=['bold']))
            # Pause before continuing the game
            time.sleep(3)
            return selection
        # Repeat the loop if invalid, to get a valid selection
        except UnboundLocalError:
            print(colored(f'\nYou entered {game_sel}. ', 'light_grey',
                          attrs=['bold']) + colored(wrong_input, 'light_cyan'))
            continue


def character_selection():
    """
    Function that runs the first part of the story
    """
    print(colored(welcome_story, 'light_grey'))
    # Pause before continuing the game
    time.sleep(3)

    # Character selection
    print(colored(char_sel_story, 'light_yellow'))
    character = game_selections(char_sel, char_invalid, *characters)
    return character


def first_story_part(character):
    """
    Function that runs the first part of the story
    """
    print(colored(path_choice_story, 'light_yellow'))

    # Path story choice for the user
    game_selections(path_req, path_invalid, *path_choices)

    # User rolls die
    path_die = roll_dice(path_roll, 6)
    # Outcome of path die roll
    if (path_die % 2) == 0:
        # Lucky path outcome for even numbers
        print(colored(path_lucky_story, 'light_grey'))
    else:
        # Unlucky path outcome for odd numbers
        panther_roll = path_unlucky_story
        # Unlucky path outcome die roll
        panther_die = roll_dice(panther_roll, 20)
        if 1 <= panther_die <= 3:
            # Game over for die rolls 1 - 3
            print(colored(panther_unlucky_outcome,
                          'light_red', attrs=['bold']))
            # Pause before continuing the game
            time.sleep(3)
            print(colored(game_over, 'light_red', attrs=['bold']))
            raise NewGame
        elif character == 'Witch':
            # Good Witch lucky path outcome for die rolls 4 - 20
            print(colored(witch_attack, 'light_grey'))
        elif character == 'Pixie':
            # Good Pixie lucky path outcome for die rolls 4 - 20
            print(colored(pixie_attack, 'light_grey'))
        elif character == 'Nymph':
            # Good Nymph lucky path outcome for die rolls 4 - 20
            print(colored(nymph_attack, 'light_grey'))
        elif character == 'Druid':
            # Good Druid lucky path outcome for die rolls 4 - 20
            print(colored(druid_attack, 'light_grey'))


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

    print(colored(cabin_choice_story, 'light_yellow'))

    # Cabin story choice for the user
    cabin_sel = game_selections(cabin_req, cabin_invalid, *cabin_choices)

    # Outcome of cabin user choice
    if cabin_sel == 'Barge':
        # User rolls die
        second_sub_roll = cabin_roll
        second_sub_die = roll_dice(second_sub_roll, 20)

        if 1 <= second_sub_die <= 4:
            # Cabin barge unlucky outcome
            print(colored(barge_unlucky_story, 'light_red', attrs=['bold']))
            # Pause before continuing the game
            time.sleep(3)
            print(colored(game_over, 'light_red', attrs=['bold']))
            raise NewGame
        else:
            # Cabin barge lucky outcome
            print(colored(barge_lucky_story, 'light_yellow'))
            barge_lucky = True

    elif cabin_sel == 'Knock':
        # User rolls die
        second_die = roll_dice(knock_roll, 6)

        # Outcome of cabin knocking die roll
        if (second_die % 2) != 0:
            # Cabin knocking lucky outcome
            print(colored(knock_lucky_story, 'light_grey'))
            knock_lucky = True
        else:
            # Cabin knocking unlucky outcome
            print(colored(knock_unlucky_story, 'light_yellow'))
            knock_lucky = False

    if (cabin_sel == 'Barge' and barge_lucky) \
            or (cabin_sel == 'Knock'
                and knock_lucky is False):
        # Cabin story unlucky choice outcome for the user
        cabin_unlucky_sel = game_selections(cabin_unlucky_req,
                                            cabin_unlucky_invalid,
                                            *cabin_unlucky_choices)
        if cabin_unlucky_sel == 'Talk':
            talk_crone = True
        else:
            ko_choice = True
            # Pause before continuing the game
            time.sleep(3)

    if (
            (cabin_sel == 'Knock' and knock_lucky) or
            (knock_lucky is False and talk_crone) or
            (cabin_sel == 'Barge' and talk_crone)
    ):
        # Crone story choice for the user
        print(colored
              (crone_choice_story, 'light_yellow'))

        crone_sel = game_selections(crone_req, crone_invalid, *crone_choices)

        if crone_sel == 'Yes':
            # Crone lucky ending option
            print(colored
                  (crone_lucky_outcome, 'light_green', attrs=['bold']))
            raise NewGame
        else:
            # Die roll for crone unlucky outcome
            print(colored(crone_unlucky_story, 'light_grey'))
            disagree = True
            # Pause before continuing the game
            time.sleep(3)

    if disagree or ko_choice:
        crone_roll = crone_unlucky_roll
        # User rolls die
        crone_die = roll_dice(crone_roll, 20)

        # Outcome of crone die roll
        if 16 <= crone_die <= 20:
            # Game over for die rolls 16 - 20
            print(colored(crone_unlucky_outcome, 'light_red', attrs=['bold']))
            # Pause before continuing the game
            time.sleep(3)
            print(colored
                  (game_over, 'light_red', attrs=['bold']))
            raise NewGame
        else:
            # Crone defeated ending option
            print(colored(crone_defeat_outcome, 'light_green', attrs=['bold']))
            raise NewGame


def gameplay():
    """
    Function that runs the full game
    """
    while True:
        try:
            # Start the game
            character = character_selection()
            # First game options
            first_story_part(character)
            # Pause before continuing the game
            time.sleep(3)
            # Second set of game options
            second_story_part()
        except NewGame:
            pass
        while True:
            # See if the user wants to play again
            restart_game()


# Run the game
gameplay()
