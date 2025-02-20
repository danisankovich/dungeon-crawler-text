# Dani Sankovich

rooms = {
    'Great Hall': {
        'directions': {
            'west': { 'name': 'Library', 'hidden': False },
            'north': { 'name': 'Villain\'s Lair', 'hidden': False },
            'east': { 'name': 'Dining Room', 'hidden': False },
        },
        'description': [
            'A grand staircase leads to the door to the Villain\'s Lair to the north.',
            'To the east is the Dining Room.',
            'To the west is the Library',
            'To the south is the castle\'s exit, should you wish to surrender.'
        ],
        'item': {
            'name': 'Sword of the Morning',
            'script': [
                'A marble statue of the Dragonlord in his human form stands at the center.',
                'In his hand is a sword with a powerful aura.',
            ],
            'investigation': [
                'Closer inspection reveals the sword to be made of metal, not stone.',
                'Power rings from its blade',
                'Pick up the sword? Y/N'
            ],
            'consequence': [
                'Sword of the Morning added to your inventory.',
            ],
            'hidden': True # hidden means something has to be done before more detail is revealed
        },
        'options': [
            'Search Statue'
        ]
    },
    'Villain\'s Lair': {
        'directions': {
            'south': { 'name': 'Great Hall', 'hidden': False },
            'north': { 'name': 'Chambers', 'hidden': True },
        },
        'description': [
            'The mighty Dragonlord stands before you.',
            'He transforms into a mighty dragon and towers over you',
            'You raise your hand and with a powerful chant, magic flows through you.',
            'Lightning arcs from your fingertips, smiting the Dragonlord. You have saved the day!',
            '!!!The End!!!'
        ],
    },
    'Library': {
        'directions': {
            'east': { 'name': 'Great Hall', 'hidden': False },
            'north': { 'name': 'Study', 'hidden': False },
        },
        'description': [
            'Ancient tomes line the shelves along the walls.',
            'The Door to the North leads to the study',
            'The Door to the East leads to the Great Hall'
        ],
        'item': {
            'name': 'Tome of Forgotten Magiks',
            'script': [
                'In the bookshelves you find the Tome of Forgotten Magiks.',
                'The text within teaches you the mighty lightning spells of legend.',
                'Pick up the tome? Y/N'
            ],
            'consequence': [
                'Tome of Forgotten Magiks added to your inventory.',
            ],
            'hidden': True
        },
        'options': [
            'Search Bookshelves'
        ]
    },
    'Dining Room': {
        'directions': {
            'west':{ 'name': 'Great Hall', 'hidden': False },
            'north': { 'name': 'Kitchen', 'hidden': False },
        },
        'description': [
            'A long table sits here, with a meal set for one.',
            'The other places.... look like they\'ve not been used in a long time.',
            'To the north is the Kitchen.',
            'To the west is the Great Hall.'
        ],
        'item': {
            'name': 'Shield of Dusk',
            'script': [
                'The Shield of Dusk, capable of reflecting the strongest of magic sits above the fireplace.',
                'You recognize its design from countless stories of legendary heroes and villains'
            ],
            'consequence': [
                'You remove the shield from its mount. It feels almost weightless in your hand.',
                'Shield of Dusk added to your inventory.'
            ],
            'consequence_alternative': [
                'You eat the Dragonlord\'s meal.',
                'It\'s disappointingly bland.'
            ]
        },
        'options': [
            'Take Shield',
            'Eat Meal'
        ]
    },
    'Kitchen': {
        'directions': {
            'south': { 'name': 'Dining Room', 'hidden': False },
        },
        'description': [
            'The Kitchen is spotless, save for some pots and utensils in the sink.',
            'Among the kitchenware you find a rack of vials containing number of potions.',
            'To the south is the Dining Room.'
        ],
        'item': {
            'name': 'Potion of Cunning',
            'script': [
                'Most of them are basic. But one catches your eye.',
                'It gives off a strong magical aura.',
                'Pick up the potion? Y/N'
            ],
            'consequence': [
                'Potion of Cunning added to your inventory.'
            ],
            'hidden': True,
            'post_script': True
        },
        'options': [
            'Search Potions'
        ],
    },
    'Study': {
        'directions': {
            'south': { 'name': 'Library', 'hidden': False },
            'down': { 'name': 'Dungeons', 'hidden': False },
            'northeast': { 'name': 'Chambers', 'hidden': True },
        },
        'description': [
            'A desk sits here, atop which lie a few stacked books.',
            'A hatch in the corner on the floor leads to the Dungeons.',
            'Something about this room picks at your brain.'
        ],
        'item': {
            'name': 'Ring of Protection',
            'script': [
                'Sitting on the desk, you spot a dazzling silver ring.',
                'Closer inspection reveals it to look remarkably similar to the fabled Ring of Protection.',
                'Slip the ring onto your finger? Y/N'
            ],
            'consequence': [
                'The ring was trapped. Not all treasures are yours for the taking.',
                'Your soul is trapped within the ring until the Dragonlord decides to free you from this fate.',
                'GAME OVER'
            ],
            'post_script': True
        }
    },
    'Chambers': {
        'directions': {
            'southwest': { 'name': 'Study', 'hidden': True },
            'south': { 'name': 'Villain\'s Lair', 'hidden': False }, 
        },
        'description': [
            'Exiting the hidden tunnel leads you to the Dragonlord\'s Chambers.',
            'An extravagant bed sits here, sheets made with perfection',
            'To the southwest is the Study.',
            'To the South is the Villain\'s Lair.'
        ],
        'item': {
            'name': 'Orb of Wonders',
            'script': [
                'Hovering above the nightstand and a sea-green orb the size of your fist.',
                'It gives off astounding magical power, the kind capable of leveling cities.',
                'you wonder if it is more power than any mortal should rightly possess.'
            ],
             'consequence': [
                'Holding the orb in your hand, you wonder if the Dragonlord is worthy of his power.',
                'Orb of Wonders added to your inventory.'
            ],
            'consequence_alternative': [
                'You understand that the Dragonlord was once a man.',
                'A mere mortal such as yourself.',
                'Too much power, even in the hands of a hero, is a path to corruption.',
                'You throw the orb against the wall, shattering it in a shower of arcane sparks.',
                'Only a fragment is left behind. You hope it will be enough for the task that awaits.',
                'Fragment of Wonder added to your inventory.'
            ],
        },
        'options': [
            'Take Orb', 'Destroy Orb'
        ]
    },
    'Dungeons': {
        'directions': {
            'up':{ 'name': 'Study', 'hidden': False },
        },
        'description': [
            'Cold and dreary, cramped cages line the walls.',
            'You wonder how many comrades have died here.',
        ],
        'options': [
            'Search Cells'
        ],
        'item': {
            'name': 'Forgotten Letter',
            'script': [
                'You spot a red stain on the wall ... you find a scrawled note so covered in blood that you can\'t read it.',
                'All that you can make out from the writing is "I Love You"',
                'Pick up the note? Y/N'
            ],
            "post_script": True,
            'consequence': [
                'You are filled with rage and fury the likes of which you have never known.',
                'It gives you purpose, and single-minded focus to tackle the challenge that lies in your future.',
                'Forgotten Letter added to your inventory.'
            ],
            'hidden': True
        }
    }
}

# 
# TODO: if they have an item in inventory that matches the name in the item 
# Category of the room, don't do the item description stuff

# also, check if you have potion of cunning in inventory when entering study. if so, secret opens
# 
# Make sure that options can only be used in a room when they are valid. So you can't search statue anywhere
# except for great hall
# just check against current_options_list
# 



# options that should always be included as valid
base_options = ['check map', 'rest', 'inventory', 'exit']
current = 'Great Hall'
current_options_list = list()
inventory = list()

def enterRoom(room_name):
    current_options_list = list()
    current = room_name
    room_obj = rooms[current]
    print(f'You find yourself standing in the {current}.')
    print()
    for desc in room_obj['description']:
        print(desc)

    print()

    if 'item' in room_obj and 'found' not in room_obj['item']:
        for line in room_obj['item']['script']:
            print(line)
    
    for direction in room_obj['directions'].keys():
        current_options_list.append(f'go {direction.lower()}')
    
    if 'options' in room_obj:
        current_options_list = current_options_list + room_obj['options']
    
    # ensure base options always come last
    current_options_list = current_options_list + base_options

    print()
    for idx, option in enumerate(current_options_list):
        print(f'{idx + 1}) {option}')
    
def show_inventory():
    print(inventory)

def library():
    enterRoom('Library')


def greatHall():
    enterRoom('Great Hall')


# current room for display and tracking purposes

def main():
    greatHall()
    # while True:
    #     print(f'You find yourself standing in the {current}')
    #     # initialize a list for dynamic purposes
    #     options = list()
    #     # base direction commands based on the keys in the current room
    #     for direction in rooms[current].keys():
    #         options.append(f'go {direction}')

    #     # concatenate direction options and base_options
    #     options = options + base_options

    #     # display all valid options for the user
    #     command = input(f'What will you do next? {options}: ')

    #     # lowercase the command for simplicity and user's sake
    #     if command.lower() == 'exit':
    #         print('Do not feel shame. Greater heroes than you have failed. Perhaps the next hero will be ... more.', end='\n\n')
    #         # end the loop
    #         break

    #     # lets the user check what the adjacent rooms are
    #     if command.lower() == 'check map':
    #         print('You check your map. The following rooms are adjacent to you: ', end='\n\n')
    #         for direction, value in rooms[current].items():
    #             print(f'{direction}: {value}')
    #         print('\n')
    #         continue


    #     if command.lower() == 'search':
    #         print("Searching the room, you don't find what you are here for. Perhaps the programmer should sleep less.", end='\n\n')
    #         continue

    #     if command.lower() == 'rest':
    #         # TODO: player recovers health after resting. Player gets 1 rest per playthrough
    #         print('You look tired. Rest your weary head for a moment. The world is dark, but here it is warm. If only for a moment.', end='\n\n')
    #         continue

    #     # if the input doesn't match earlier commands, split on the space
    #     separated = command.split(' ')

    #     # check that the format of input matches 'go <direction>' format and that the direction
    #     # exists on the current room. If either reason is invalid, tell the user
    #     if len(separated) != 2 or separated[0].lower() != 'go' or not separated[1].lower() in rooms[current].keys():
    #         print('Invalid command', end='\n\n')
    #         continue

    #     # change current room, using lower() to normalize the input to the rooms keys
    #     current = rooms[current][separated[1].lower()]
    #     # alert the user, then restart the loop
    #     print('Moving to a new room ...', end='\n\n')

    #     # if player enters the villain's lair, they win the game
    #     if current == "Villain's Lair":
    #         # TODO: implement checks to ensure the player has collected all necessary items to win the battle
    #         # if they have all items, give them the room description
    #         # otherwise give them the failure description
    #         # end the program upon victory
    #         break

main()