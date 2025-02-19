# Dani Sankovich

rooms = {
    'Great Hall': {'south': 'Bedroom', 'north': "Villain's Lair"},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'},
    "Villain's Lair": {'south': 'Great Hall'},
    "Library": {},
    "Kitchen": {},
    "Study": {},
    "Chambers": {},
    "Dungeons": {}
}

# options that should always be included as valid
base_options = ['check map', 'search', 'rest', 'exit']
current = 'Great Hall'

def library():
    current = 'Library'

def greatHall():
    current = 'Great Hall'

# current room for display and tracking purposes

while True:
    print(f'You find yourself standing in the {current}')
    # initialize a list for dynamic purposes
    options = list()
    # base direction commands based on the keys in the current room
    for direction in rooms[current].keys():
        options.append(f'go {direction}')

    # concatenate direction options and base_options
    options = options + base_options

    # display all valid options for the user
    command = input(f'What will you do next? {options}: ')

    # lowercase the command for simplicity and user's sake
    if command.lower() == 'exit':
        print('Do not feel shame. Greater heroes than you have failed. Perhaps the next hero will be ... more.', end='\n\n')
        # end the loop
        break

    # lets the user check what the adjacent rooms are
    if command.lower() == 'check map':
        print('You check your map. The following rooms are adjacent to you: ', end='\n\n')
        for direction, value in rooms[current].items():
            print(f'{direction}: {value}')
        print('\n')
        continue


    if command.lower() == 'search':
        print("Searching the room, you don't find what you are here for. Perhaps the programmer should sleep less.", end='\n\n')
        continue

    if command.lower() == 'rest':
        # TODO: player recovers health after resting. Player gets 1 rest per playthrough
        print('You look tired. Rest your weary head for a moment. The world is dark, but here it is warm. If only for a moment.', end='\n\n')
        continue

    # if the input doesn't match earlier commands, split on the space
    separated = command.split(' ')

    # check that the format of input matches 'go <direction>' format and that the direction
    # exists on the current room. If either reason is invalid, tell the user
    if len(separated) != 2 or separated[0].lower() != 'go' or not separated[1].lower() in rooms[current].keys():
        print('Invalid command', end='\n\n')
        continue

    # change current room, using lower() to normalize the input to the rooms keys
    current = rooms[current][separated[1].lower()]
    # alert the user, then restart the loop
    print('Moving to a new room ...', end='\n\n')

    # if player enters the villain's lair, they win the game
    if current == "Villain's Lair":
        # TODO: implement checks to ensure the player has collected all necessary items to win the battle
        print('The mighty Dragonlord stands before you. You raise your hand and with a powerful chant, magic flows through you.')
        print('Lightning arcs from your fingertips, smiting the Dragonlord. You have saved the day!')
        print('!!!The End!!!')
        # end the program upon victory
        break

