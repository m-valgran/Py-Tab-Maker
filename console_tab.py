# Input/Output
from tabmaker_io import output_controller
from tabmaker_io.input_controller import listen_key_release
from tabmaker_io.output_controller import print_at, clear_console
# Pynput keyboard
from pynput import keyboard
# Colorama
from colorama import Fore
from colorama import Style
# Text Support
from text_support.text_support import replace_at
# Datetime
from datetime import datetime
# Exit
from sys import exit

def write_in_tab():
    while True:
        key_released = listen_key_release()
        if(type(key_released) == keyboard._win32.KeyCode):
            return key_released.char
        elif key_released == keyboard.Key.backspace:
            return '-' 
                
def display_interactive_tab(x,y,tuning):
    # Defining list to store each istring
    istring_quantity = len(tuning)
    istrings = []
    
    # Reversing tuning in order to print the lower notes above the higher ones
    tuning.reverse()
    
    # Setting up the starter empty tab
    for index, istring in enumerate(tuning):
        # Some notes could have a '#' so they will be two char long
        spacing = ' ' if len(istring) == 1 else '' 
        istrings.append(f'{istring}{spacing}|---')

    # Defining selected position dictionary
    selected_position = {'x':4,'y':0}
    while True:
        # Highlights the selected character in red
        highlight_and_display(x,y,istrings, selected_position, 'RED')
        
        # Listening key release
        key_released = listen_key_release()  
        match key_released:
            case keyboard.Key.up:
                # Move UP
                selected_position['y'] -= 1 if selected_position['y'] > 0 else 0
            case keyboard.Key.down:
                # Move DOWN
                selected_position['y'] += 1 if selected_position['y'] < istring_quantity-1 else 0
            case keyboard.Key.left:
                # Move LEFT
                selected_position['x'] -= 1 if selected_position['x'] > 4 else 0
            case keyboard.Key.right:
                # Move RIGHT
                selected_position['x'] += 1 if selected_position['x'] < len(istrings[0])-2 else 0
            case keyboard.Key.enter:
                # Highlights the selected character in green
                highlight_and_display(x,y,istrings, selected_position, 'GREEN')
                
                # Invokes write_in_tab to get a new value
                new_value = write_in_tab()
                
                # Replaces old value in istrings with new_value
                istring = istrings[selected_position['y']]
                index = selected_position['x']
                updated_istring = replace_at(istring, index, new_value)
                istrings[selected_position['y']] = updated_istring
            case keyboard.Key.space:
                # Stretching the tab
                istrings = stretch_istrings(istrings)
            case keyboard.Key.backspace:
                f = open(f"tab_{datetime.now().microsecond}.txt", "w")
                f.write('\n'.join(istrings))
                f.close()
            case keyboard.Key.end:
                exit()
        
# Adds an extra '-' character for each instrument string
def stretch_istrings(istrings):
    for index, _ in enumerate(istrings):
        istrings[index] += '-'
    return istrings
    
# Highligts a character at the given coordinates
def highlight_and_display(x,y,istrings,selected_position,color):
    clear_console()
    print_hints(x,y)
    # Defining a copy to display without overwriting the
    # original grid when printing cursor position  
    display = istrings.copy()
    console_color = getattr(Fore, color)
    for i, istring in enumerate(istrings):
        # Case of selected istring
        if selected_position['y'] == i:
            # takes the value at the selected position and prints it in the given color
            value = istrings[selected_position['y']][selected_position['x']]
            highlighted_value = f'{console_color}{value}{Style.RESET_ALL}' 
            display[i] = replace_at(istring, selected_position['x'], highlighted_value)
        # Case of not selected istring
        else:
            display[i] = replace_at(istring, selected_position['x'], istring[selected_position['x']])
    # Prints the coloured (highlighted) character
    print_at(x,y+2,'\n'.join(display))

def print_hints(x,y):
    move = f'{getattr(Fore, "BLUE")}[ARROWS]{Style.RESET_ALL} Move'
    edit = f'{getattr(Fore, "GREEN")}[ENTER]{Style.RESET_ALL} Edit'
    stretch = f'{getattr(Fore, "CYAN")}[SPACE]{Style.RESET_ALL} Stretch'
    export = f'{getattr(Fore, "YELLOW")}[BACKSPACE]{Style.RESET_ALL} Export txt'
    exit = f'{getattr(Fore, "RED")}[END]{Style.RESET_ALL} Exit'
    print_at(x,y,f'{move} | {edit} | {stretch} \n{export} | {exit}')