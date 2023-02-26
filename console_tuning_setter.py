# The following import logic should be avoided.
import sys
sys.path.append('../')

# Console Menu
from console_menu import display_option_menu
# Input/Output
from tabmaker_io.input_controller import listen_key_release
from tabmaker_io.output_controller import print_at, clear_console
# Pynput Keyboard
from pynput import keyboard
# Colorama
from colorama import Fore
from colorama import Style

NOTES = ['A ','A#','B ','C ','C#','D ','D#','E ','F ','F#','G ','G#']

def set_tab(x,y):
    # Defining the main tuning_list list
    tuning_list = []
    
    # Defining positions of elements in screen
    notes_pos = {'x':x,'y':y+2}
    option_menu_pos = {'x':x,'y':y+3}
    
    # Defining a set of button hints
    enter_color = getattr(Fore, 'MAGENTA')
    spacebar_color = getattr(Fore, 'BLUE')
    reset_s = Style.RESET_ALL
    hints = f'{enter_color}[Enter]{reset_s} Add note\n{spacebar_color}[Spacebar]{reset_s} Save tuning'
    
    stop_input = False
    while not stop_input:
        # Printing title
        print_at(x,y,"Set custom tuning:")

        # Selecting a new note to be pushed into the list
        omp_x = option_menu_pos['x']
        omp_y = option_menu_pos['y']
        note = display_option_menu(omp_x, omp_y, NOTES, display_type='s',clear_console_bool=False)
        note = note.strip()
        tuning_list.append(note)

        # Printing the current tuning_list
        selected_notes = f'Current tuning: [{" ".join(tuning_list)}]'
        print_at(notes_pos['x'], notes_pos['y'], selected_notes)
        
        # Printing the hints
        print_at(option_menu_pos['x'], option_menu_pos['y'], hints)
        
        # either continue adding notes [Enter] 
        # or save the tuning_list [Space]
        stop_options = False
        while not stop_options:
            key_released = listen_key_release()
            match key_released:
                case keyboard.Key.enter:
                    stop_options = True
                case keyboard.Key.space:
                    stop_options = True
                    stop_input = True
                case _:
                    pass
        
        # Instead of clearing the whole console, it just clears the hints
        # in order to preven the chosen notes list to be hidden
        hide_hints(option_menu_pos['x'], option_menu_pos['y'], hints)

    clear_console()
    return tuning_list

def hide_hints(x,y,hints):
    print_at(x, y, ' '*len(hints.split('\n')[0])+'\n'+' '*len(hints.split('\n')[1]))