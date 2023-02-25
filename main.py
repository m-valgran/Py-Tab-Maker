from sys import exit
from console_menu import display_option_menu
from console_tuning_presets import choose_preset
from console_tuning_setter import set_tab
from console_tab import display_interactive_tab

X_POS = 1
Y_POS = 1

# User chooses either use a preset or create a tuning
tuning_choice = display_option_menu(X_POS,Y_POS,['Tuning preset','Custom tuning','Exit'],fore_color='YELLOW')
tuning_list = []
match tuning_choice:
	case 'Tuning preset':
		# User picks tuning from a preset list
		tuning_list = choose_preset(X_POS,Y_POS)
	case 'Custom tuning':
		# User inputs a tuning manually
		tuning_list = set_tab(X_POS,Y_POS)
	case 'Exit':
		exit()

# User writes the tab
display_interactive_tab(X_POS,Y_POS,tuning_list)