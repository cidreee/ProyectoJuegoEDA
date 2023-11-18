"""
@author: Christopher Oswaldo Márquez Reyes
@author: Valeria Marian Andrade Monreal
"""

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.location = 'start'
        self.status_effects = []


myPlayer = Player()


def title_screen_selections():
    option = input(" > ")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command...")
        option = input(" > ")
        if option.lower() == "play":
            start_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def tittle_screen():
    os.system('clear')
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
    pass

