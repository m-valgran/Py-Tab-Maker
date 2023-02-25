# Regex
import re
# Input/Output
from tabmaker_io import output_controller
from tabmaker_io.output_controller import print_at, clear_console
from tabmaker_io.input_controller import listen_key_release
# Pynput Keyboard
from pynput import keyboard
# Colorama
from colorama import Fore
from colorama import Style
# Text Support
from text_support.text_support import replace_at

# Displays an interactive list of options that can be controlled with arrow keys
def display_option_menu(x,y,option_list, fore_color="RED", display_type='vertical',clear_console_bool=True):
    selected_index = 0
    selected_option = option_list[selected_index]
    need_regex = True
    
    # Settings according the given display type
    match display_type.lower():
        case 'vertical' | 'v':
            last_char = '\n'
            key_next = keyboard.Key.down
            key_prev = keyboard.Key.up          
        case 'horizontal' | 'h':
            last_char = ' '
            key_next = keyboard.Key.right
            key_prev = keyboard.Key.left
        case 'single' | 's':
            need_regex = False
            key_next = keyboard.Key.right
            key_prev = keyboard.Key.left
    
    # For horizontal and vertical lists, a regex will match the selected option and highlight 
    # (colour) the currently chosen one, adding a '*' character in bewtween the '[ ]'
    display = ''.join(f'[ ]{option}{last_char}' for option in option_list) if need_regex else ''

    while True:
        # Printing horizontal or vertical list
        if need_regex:
            option_regex = re.compile(f'\[ \]{selected_option}{last_char}')
            console_color = getattr(Fore, fore_color.upper())
            istring_literal = option_regex.sub(f'{console_color}[*]{selected_option}{Style.RESET_ALL}{last_char}',display)
            istring_literal = replace_at(istring_literal, len(istring_literal)-1, '')
            print_at(x,y,istring_literal)
        # Printing single element list
        else:
            print_at(x,y,f'<< {selected_option} >>')
        
        # Chosing next or prev option, or pressing enter to submit
        key_released = listen_key_release()
        if key_released == key_prev:
            selected_index -= 1 if selected_index > 0 else 0
            selected_option = option_list[selected_index]
        elif key_released == key_next:
            selected_index += 1 if selected_index + 1 < len(option_list) else 0
            selected_option = option_list[selected_index]
        elif key_released == keyboard.Key.enter:
            break
    
    if(clear_console_bool):
        clear_console()

    return selected_option
