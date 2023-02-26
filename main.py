# Sys exit
from sys import exit
# Console
from console_menu import display_option_menu
from console_tuning_presets import choose_preset
from console_tuning_setter import set_tab
from console_tab import display_interactive_tab
# Colorama
from colorama import Fore
from colorama import Style

X_POS = 1
Y_POS = 1

print(f'{getattr(Fore, "CYAN")}',end='')
print("----------~ PY TAB MAKER ~----------")
print("A terminal tab writer by Valentin G.")
print("*==================================*")
print(Style.RESET_ALL)

# User chooses either use a preset or create a tuning
tuning_choice = display_option_menu(X_POS,Y_POS+3,['Use tuning preset','Use custom tuning','Exit'],fore_color='YELLOW')
tuning_list = []
match tuning_choice:
	case 'Use tuning preset':
		# User picks tuning from a preset list
		tuning_list = choose_preset(X_POS,Y_POS)
	case 'Use custom tuning':
		# User inputs a tuning manually
		tuning_list = set_tab(X_POS,Y_POS)
	case 'Exit':
		exit()

# User writes the tab
display_interactive_tab(X_POS,Y_POS,tuning_list)