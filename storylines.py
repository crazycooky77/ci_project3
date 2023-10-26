"""
This file includes all the (non-function) story texts
for Woodlands and Witches
"""


# character_selection function texts
welcome_story = 'Welcome to Woodlands and Witches! Let\'s begin our game\n'
char_sel_story = '''You can choose between 4 characters:
1) A Witch with powerful magical abilities
2) A Druid who can transform into a jaguar
3) A mischievous Pixie who attacks with pixie dust
4) A Nymph, who is a friend to, and will be aided by, trees\n'''
char_sel = 'Type in the number or character type to make your selection: '
char_invalid = 'Please type 1 or Witch, 2 or Druid, 3 or Pixie, 4 or Nymph'
characters = ['Witch', 'Druid', 'Pixie', 'Nymph']

# first_story_part function texts
path_choice_story = '''You wake up in the middle of a dark forest.
There are 3 paths ahead of you:
1) One path leads to a Cave.
2) One leads to a Clearing.
3) The last path leads to a River.
What do you choose?\n'''
path_req = 'Type in the number or location to make your selection: '
path_invalid = 'Please type 1 or Cave, 2 or Clearing, 3 or River'
path_choices = ['Cave', 'Clearing', 'River']
path_roll = '''Roll the die to determine what happens
when you arrive at your destination.'''
'''A giant panther appears, goes up to you,
and nudges your hand with it's head.
It wants to make friends!\n'''
path_lucky_story = '''A giant panther appears, goes up to you,
and nudges your hand with it's head.
It wants to make friends!\n'''
path_unlucky_story = '''A giant panther appears,
looking at you menacingly...
What will you do? Roll the die!\n'''
witch_attack = '''You send a huge blast of arcane magic
at the big cat and defeat it.
It agrees to help you on your quest.\n'''
pixie_attack = '''You blow a huge cloud of pixie dust
into the big cat's face.
It becomes charmed by you and your dust,
and starts following you around.\n'''
nymph_attack = '''You get your tree friends to help you.
They surround the big cat, who jumps up the branches and climbs the tree.
It falls asleep on the tree limbs, thanking you for the assistance.
It wants to repay the favour.\n'''
druid_attack = '''You transform into a jaguar
and make friends with the big cat.
It joins you on your journey!\n'''

# second_story_part function texts
cabin_choice_story = '''You continue on and see a little cabin
with smoke coming out of the chimney.
Do you 1) Knock on the door, or 2) Barge right in?\n'''
cabin_req = 'Type in the number or word to make your selection: '
cabin_invalid = 'Please type 1 or Knock, 2 or Barge'
cabin_choices = ['Knock', 'Barge']
cabin_roll = '''Roll the die to see
what awaits you inside the cabin.'''
barge_unlucky_story = '''You barge in and the old crone inside
sends a blast of magic your way.'''
barge_lucky_story = '''You barge in and tackle the old crone inside.
Do you 1) Talk to her, or 2) try to Knock her Out (Knockout)?\n'''
knock_roll = 'Roll the die to see who opens the door.'
knock_lucky_story = '''An old crone opens the door
and warmly welcomes you inside.'''
knock_unlucky_story = '''An old crone opens the door
and looks at you suspiciously.
Do you 1) Talk to her or 2) try to Knock her Out (Knockout)?\n'''
cabin_unlucky_req = 'Type in the number or word to make your selection: '
cabin_unlucky_invalid = 'Please type 1 or Talk, 2 or Knockout'
cabin_unlucky_choices = ['Talk', 'Knockout']
crone_choice_story = '''The crone has seen you in her visions previously.
She wants to train you as her protege...
Do you agree?\n'''
crone_req = 'Type in 1 or Yes, 2 or No, to make your selection: '
crone_invalid = 'Please type 1 or Yes, 2 or No'
crone_choices = ['Yes', 'No']
crone_unlucky_story = '''The crone can\'t risk anyone else
finding her cabin and attacks you.\n'''
crone_unlucky_roll = '''Roll the die to see
if you\'re able to overpower the old crone!'''

# Outcomes
panther_unlucky_outcome = '''You try attacking the big cat,
but you're too slow.
It swipes at you with a giant paw,
and everything turns black!\n'''
crone_lucky_outcome = '''You begin learning everything
you can from your mentor.
Your story ends here... for now!'''
crone_unlucky_outcome = '''You try to defend yourself,
but the old crone overcomes you.
You're unable to stand against her might!\n'''
crone_defeat_outcome = '''You defeat the crone, take over her cabin,
and start looking through all of her ancient tomes.
You learn all you can of her magic and enchantments.
Your story ends here... for now!'''
game_over = 'You died... Game Over'
