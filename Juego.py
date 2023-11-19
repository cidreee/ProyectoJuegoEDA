"""
@author: Christopher Oswaldo Márquez Reyes
@author: Valeria Marian Andrade Monreal
"""


import sys


class Player:
    def __init__(self, name='', hp=0, location='start', status_effects=None, items=None):
        self.name = name
        self.hp = hp
        self.location = location
        self.status_effects = status_effects if status_effects is not None else []
        self.items = items if items is not None else []


myPlayer = Player()


def title_screen_selections():
    option = input('')
    if option.lower() == 'play':
        start_game()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print('Please enter a valid command...')
        option = input('> ')
        if option.lower() == 'play':
            start_game()
        elif option.lower() == 'help':
            help_menu()
        elif option.lower() == 'quit':
            sys.exit()


def title_screen():
    print('')
    print('############################')
    print('# Welcome to ------------- #')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    print('                            ')
    title_screen_selections()


def help_menu():
    print('')
    print('############################')
    print('# Welcome to ------------- #')
    print('############################')
    print('- Use up, down, left, right to move')
    print('- Type your command to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun')
    title_screen_selections()


def start_game():
    player_name = input('\nHello there, What is your name? ')
    myPlayer = Player(name=player_name)
    print('That\'s a nice name')
    print(f'Welcome, {myPlayer.name}! Let\'s start the game.')


def ruta_1():
    pass


def ruta_2():
    pass


def ruta_3():
    pass


def ruta_4():
    pass


title_screen()

