# Colorama Init
from colorama import init as colorama_init
# Operating System
from os import system, name

# Starting up colorama
colorama_init()

# Clears the console
def clear_console():
    _ = system('cls') if name == 'nt' else system('clear')

# Prints a string at the given coordinates of the console
def print_at (x, y, text):
    print(f"\033[{y};{x}H{text}")