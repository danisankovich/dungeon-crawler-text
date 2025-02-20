# Dani Sankovich
import sys

rooms = {
    'Great Hall': {
        'directions': {
            'west': { 'name': 'Library', 'hidden': False },
            'north': { 'name': 'Villain\'s Lair', 'hidden': False },
            'east': { 'name': 'Dining Room', 'hidden': False },
            'south': {'name': 'exit', 'hidden': False}
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
            ],
            'consequence': [
                'You take the sword from the statue\'s grasp. You can feel its power.',
                '\nSword of the Morning added to your inventory.',
            ],
            'found': False,
        },
        'options': [
            'Search Statue'
        ]
    },
    'Library': {
        'directions': {
            'east': { 'name': 'Great Hall', 'hidden': False },
            'north': { 'name': 'Study', 'hidden': False },
        },
        'description': [
            'The Door to the North leads to the study',
            'The Door to the East leads to the Great Hall'
        ],
        'item': {
            'name': 'Tome of Forgotten Magiks',
            'script': [
                'Ancient tomes line the shelves along the walls.',
            ],
            'investigation': [
                'In the bookshelves you find the Tome of Forgotten Magiks.',
            ],
            'consequence': [
                'The text within teaches you the mighty lightning spells of legend.',
                '\nTome of Forgotten Magiks added to your inventory.',
            ],
            'found': False,
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
                'A shield hangs above the fireplace.',
            ],
            'investigation': [
                'Upon closer inspection, you recognize the shield from your history books.',
                'It is the Shield of Dusk, capable of reflecting even the strongest of magic.',
                'Countless heroes and villains of legend wielded it.'
            ],
            'consequence': [
                'You remove the shield from its mount. It feels almost weightless in your hand.',
                'The Dragonlord\'s arrogance in leaving this as decoration will be his downfall.',
                '\nShield of Dusk added to your inventory.'
            ],
            'found': False,
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
            ],
            'investigation': [
                'The potion in question shimmers in the light.',
                'It is a light blue liquid, like gazing into a clear blue sky trapped in a bottle.'
            ],
            'consequence': [
                'This might help you find what others hoped to remain hidden.',
                '\nPotion of Cunning added to your inventory.'
            ],
            'found': False,
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
        'options': ['inspect ring'],
        'item': {
            'name': 'Ring of Protection',
            'script': [
                'Sitting on the desk, you spot a dazzling silver ring.',
            ],
            'investigation': [
                'Closer inspection reveals it to look remarkably similar to the fabled Ring of Protection.',
                'This ring, when worn, shields the wearer from physical harm.'
            ],
            'consequence': [
                'As you slide the ring onto your finger you realize your mistake.',
                'The ring was a trap. Not all treasures are yours for the taking.',
                '\nYour soul is trapped within the ring until the Dragonlord decides to free you from this fate.',
                '\nGAME OVER'
            ],
            'found': False,
        }
    },
    'Chambers': {
        'directions': {
            'southwest': { 'name': 'Study', 'hidden': False },
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
                '\nHovering above the nightstand and a sea-green orb the size of your fist.',
                '\nIt gives off astounding magical power, the kind capable of leveling cities.',
                '\nYou wonder if it is more power than any mortal should rightly possess.',
                '\nYou briefly wonder if you should destroy it, lest it lead you down a path you cannot turn back from.',
                '\nBut to let such power go.........could it be a waste?'
            ],
            'investigation': [
                'As you approach, the orb\'s light intensifies.'
            ],
            'consequence': [
                'Holding the orb in your hand, you wonder if the Dragonlord is worthy of his power.',
                'Perhaps someone more worthy should take his place',
                'Orb of Wonders added to your inventory.'
            ],
            'consequence_alternative': [
                'You understand that the Dragonlord was once a man.',
                'A mere mortal such as yourself who fell to the same darkness that entices all humankind.',
                'Too much power, even in the hands of a hero, is a path to corruption.',
                'You throw the orb against the wall, shattering it in a shower of arcane sparks.',
                'Only a fragment is left behind. You hope it will be enough for the task that awaits.',
                'Fragment of Wonder added to your inventory.'
            ],
            'found': False,
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
            'Search Cell'
        ],
        'item': {
            'name': 'Forgotten Letter',
            'script': [
                'You spot a red stain on the wall in one of the cells ... '
            ],
            'investigation': [
                'You hesitantly search the bloody cell.',
                'Inside, you find a scrawled note hidden between cracks in the stone wall.',
            ],
            'consequence': [
                'The note is so covered in dried blood that you can\'t read it.',
                'All that you can make out from the writing is "I Love You"',
                '\nUpon reading the message you are filled with rage and fury the likes of which you have never known.',
                'It gives you purpose, and single-minded focus to tackle the challenge that lies in your future.',
                '\nForgotten Letter added to your inventory.'
            ],
            'found': False,
        }
    }
}


# options that should always be included as valid
base_options = ['check map', 'rest', 'inventory', 'exit']

# state-based variables
current = 'Great Hall'
current_options_list = list()
inventory = list()
potion_drank = False
orb_status = ''

# function to change a players current room and update state as necessary
# sets up available commands, descriptions, item details, etc.
def enter_room(room_name):
    if room_name == 'Villain\'s Lair':
        final_stage()
    if room_name == 'exit':
        exit()
    else:
        global current_options_list
        global current
        global potion_drank
        current_options_list = list()
        current = room_name
        room_obj = rooms[current]
        
        print(f'You find yourself standing in the {current}.\n')
        
        for desc in room_obj['description']:
            print(desc)

        print()

        if 'item' in room_obj and room_obj['item']['found'] == False:
            for line in room_obj['item']['script']:
                print(line)
        
        for direction in room_obj['directions'].keys():
            if room_obj['directions'][direction]['hidden'] == False:
                current_options_list.append(f'go {direction.lower()}')
        
        if 'options' in room_obj:
            current_options_list = current_options_list + room_obj['options']
        
        # ensure base options always come last
        current_options_list = current_options_list + base_options

        # normalize list by lowercasing all items
        current_options_list = [item.lower() for item in current_options_list]
        print()

        # display all valid options for the user
        for idx, option in enumerate(current_options_list):
            print(f'{idx + 1}) {option}')

        if room_name == 'Study' and 'Potion of Cunning' in inventory and potion_drank == False:
            drink_potion()

# Function to display final text and determine win/loss based on the players inventory when they enter the villain's lair
def final_stage():
    if len(inventory) < 6:
        script = [
            'The Dragonlord rises from his throne.',
            'He stands head and shoulders taller than you, with armor black as night.',
            'He laughs. "So you are the one who has been making all that noise."',
            'You ready yourself to fight.',
            'But with a flick of the Dragonlord\'s wrist, you are flung backwards.',
            'Without the six items from the Dragonlord\'s keep you stand no chance against him.',
            'GAME OVER'
        ]
    else:
        script = [
            'The mighty Dragonlord stands before you.',
            'Noticing the legendary items he stole now on your person, his eyes widen in fear.',
            'Realizing his mistake, he transforms into a mighty dragon and towers over you.',
            'Undaunted, you raise your hand and with a powerful chant, magic flows through you.',
            'Lightning arcs from your fingertips, smiting the Dragonlord in a single blow.',
            'You have saved the day!',
        ]

        if orb_status == 'taken':
            script = script + [
                '...',
                '...',
                '...',
                'The orb speaks to you.',
                'Not with words, but with ideas.',
                'With its power, you can reign supreme. You alone are worthy of the throne.',
                'Thoughts of heroism and justice flee your mind.',
                'A new age, with you at the helm, shall begin'
            ]
        script.append('!!!The End!!!')

    for line in script:
        print(f'\n {line}')
    
    sys.exit(0)
        
# display the players inventory
def show_inventory():
    global inventory
    print()
    if len(inventory) == 0:
        print('Inventory Is Empty')
    else:
        for idx, item in enumerate(inventory):
            print(f'{idx + 1}) {item}')

# display current room and adjacent rooms to player
def check_map(current_room):
    print('\nYou check your map. \n')
    print(f'Current Room: {current_room}')
    for direction, room in rooms[current_room]['directions'].items():
        if room['hidden'] != True:
            print(f'{direction}: {room['name']}')

# function for handling drinking of a specific potion in inventory to access the secret room
def drink_potion():
    global potion_drank
    print('\nYou get the sense that you are missing something.')
    print('\nPerhaps drinking some of that potion would help.')
    response = ''
    
    while response.lower() not in ['y', 'n']:
        response = input('\nDrink the Potion of Cunning? Y/N: ')
    
    if response.lower() == 'y':
        print('\nYou drink some of the potion of cunning.'),
        print('\nThe hidden path to the Dragonlord\'s Chambers appears.')
        # update state and global object
        potion_drank = True
        rooms['Study']['directions']['northeast']['hidden'] = False
        current_options_list.insert(0, 'go northeast')
    if response.lower() == 'n':
        print('\nMaybe best to save it for now.')
        current_options_list.append('drink potion')
    
    # show the options list again since it may have been updated
    print()
    for idx, option in enumerate(current_options_list):
        print(f'{idx + 1}) {option}')

# 
# 
# 
# 
# 
# TODO find a way to combine these search functions so that you can just take the item data. 
# Should be easier once you get them all written out
# 
# 
# Comment them all
# 
# 
# 

def search_statue():
    print()
    item = rooms['Great Hall']['item']
    if item['found'] == True:
        print('The statue\'s hand is empty. You have already found the sword')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nPick up the sword? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        item['found'] = True
        inventory.append(item['name'])
    if response.lower() == 'n':
        print('You leave the sword where you found it')

def search_bookshelves():
    print()
    item = rooms['Library']['item']
    if item['found'] == True:
        print('Now that the book is in your possession, you do not sense any other tomes worth mentioning.')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nPick up the book? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        item['found'] = True
        inventory.append(item['name'])
    if response.lower() == 'n':
        print('You leave the book where you found it')

def search_potions():
    print()
    item = rooms['Kitchen']['item']
    if item['found'] == True:
        print('You have already found the Potion of Cunning. No other potions capture your interest.')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nPick up the potion? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        item['found'] = True
        inventory.append(item['name'])
    if response.lower() == 'n':
        print('You leave the potion where you found it')

def search_cell():
    print()
    item = rooms['Dungeons']['item']
    if item['found'] == True:
        print('You have the note in hand. You want to get out of here.')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nPick up the note? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        item['found'] = True
        inventory.append(item['name'])
    if response.lower() == 'n':
        print('You leave the note where you found it')

def take_shield():
    print()
    item = rooms['Dining Room']['item']
    if item['found'] == True:
        print('You have the shield already.')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nRemove the shield from the wall? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        item['found'] = True
        inventory.append(item['name'])
    if response.lower() == 'n':
        print('You leave the shield where you found it')

# a trap for unwary players, which can lead to a game over.
# In the future, maybe implement a dice roll system to determine if they spot the trap
# also in the future, maybe if they drank the potion, they can avoid the trap
def inspect_ring():
    print()
    item = rooms['Study']['item']
   
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nSlip the ring onto your finger? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        sys.exit(0)
    if response.lower() == 'n':
        print('You leave the ring where you found it')

# Player can keep the Orb item, setting them to the "Evil" ending
def take_orb():
    global orb_status
    print()
    item = rooms['Chambers']['item']
    if item['found'] == True:
        if orb_status == 'taken':
            print('You have the orb in your possession already.')
        if orb_status == 'broken':
            print('You have the last fragment of the orb in your possession already.')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nTake the orb for yourself? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence']:
            print(line)
        item['found'] = True
        orb_status = 'taken'
        inventory.append(item['name'])
    if response.lower() == 'n':
        print('You leave the orb where you found it')

# player has option to destroy an item and take a piece of it, giving the, the "Good" ending
def destroy_orb():
    global orb_status
    print()
    item = rooms['Chambers']['item']
    if item['found'] == True:
        if orb_status == 'taken':
            print('You have the orb in your possession already.')
        if orb_status == 'broken':
            print('You have the last fragment of the orb in your possession already.')
        return
    for line in item['investigation']:
        print(line)
    response = ''

    while response.lower() not in ['y', 'n']:
        response = input('\nDestroy the orb? Y/N: ')
    
    print()
    if response.lower() == 'y':
        for line in item['consequence_alternative']:
            print(line)
        item['found'] = True
        orb_status = 'broken'
        inventory.append('Fragment of Wonder')
    if response.lower() == 'n':
        print('You leave the orb where you found it')

# function for when a user surrenders the game
def exit():
    print('\nDo not feel shame. Greater heroes than you have failed.')
    print('\nPerhaps the next hero will be ... more.')
    print('\nGAME OVER')
    sys.exit(0)

# initialization function
def main():
    rest_counter = 0
    meal_eaten = False

    print('The Dragonlord has expanded his reign of terror.')
    print('Brave hero, travel through his castle and seek out the legendary treasures he has stolen.')
    print('Turn those 6 powerful artifacts against him and save the world.')
    print('But be warned. Fail to collect the 6 artifacts, and you will surely fail.')

    # initialize in the Great Hall
    enter_room('Great Hall')

    while True:
        global current_options_list
        global current
        # lowercase for input normalization
        command = input('\nWhat will you do next?: ').lower()

        # if command is not in the valid options list for the room, print invalid and give a new input prompt
        if command not in current_options_list:
            print('\n!!!Invalid command!!!')

        # lowercase the command for simplicity and user's sake
        elif command == 'exit':
            exit()
        
        # display inventory
        elif command == 'inventory':
            show_inventory()

        # lets the user check what the current and adjacent rooms are
        elif command == 'check map':
            check_map(current)

        # a fun command to add some flavor to the game, with added penalty
        elif command == 'rest':
            rest_counter += 1
            if rest_counter >= 3:
                print('\nToo much time has been wasted.')
                print('The Dragonlord has seen his evil plan to its end.')
                print('\nGAME OVER')
                break

            print('\nYou look tired. Rest your weary head for a moment.')
            print('The world is dark, but here it is warm. If only for a moment.')
            

        # START room-specific command functions: the various functions that can take place only in specific rooms
        elif command == 'search statue':
            search_statue()
        
        elif command == 'search bookshelves':
            search_bookshelves()
        
        elif command == 'search potions':
            search_potions()

        elif command == 'search cell':
            search_cell()
        
        elif command == 'take shield':
            take_shield()
        
        elif command == 'take orb':
            take_orb()

        elif command == 'destroy orb':
            destroy_orb()

        elif command == 'inspect ring':
            inspect_ring()
        
        elif command == 'eat meal':
            print()
            if meal_eaten == False:
                print('You eat the Dragonlord\'s meal.')
                print('It\'s disappointingly bland.')
                meal_eaten = True
            else:
                print('The plates at the table are empty.')
        
        elif command == 'drink potion':
            drink_potion()
        # END room-specific command functions
        
        else:
            # if the input doesn't match earlier commands, split on the space
            separated = command.split(' ')

            # change current room
            room_name = rooms[current]['directions'][separated[1].lower()]['name']
            # alert the user, change rooms, then restart the loop in the new room
            print('\nMoving to a new room ...\n')
            enter_room(room_name)

main()