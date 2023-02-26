from tabmaker_io.output_controller import print_at
from console_menu import display_option_menu

PRESETS = [
	{
	'name':'E guitar',
	'tuning_list':['E','A','D','G','B','E']
	},
	{
	'name':'Drop D guitar',
	'tuning_list':['D','A','D','G','B','E']
	},
	{
	'name':'D# guitar',
	'tuning_list':['D#','G#','C#','F#','A#','D#']
	},
	{
	'name':'D guitar',
	'tuning_list':['D','G','C','F','A','D']
	},
	{
	'name':'C# guitar',
	'tuning_list':['C#','F#','B','E','G#','C#']
	},
	{
	'name':'C guitar',
	'tuning_list':['C','F','A#','D#','G','C']
	},
	{
	'name':'E bass',
	'tuning_list':['E','A','D','G']
	},
	{
	'name':'Drop D bass',
	'tuning_list':['D','A','D','G']
	},
	{
	'name':'D# bass',
	'tuning_list':['D#','G#','C#','F#']
	},
	{
	'name':'D bass',
	'tuning_list':['D','G','C','F']
	},
	{
	'name':'C# bass',
	'tuning_list':['C#','F#','B','E']
	},
	{
	'name':'C bass',
	'tuning_list':['C','F','A#','D#']
	},
]

def choose_preset(x,y):
	preset_name_list = []
	for i, preset in enumerate(PRESETS):
		preset_name_list.append(preset['name'])

	# Printing title
	print_at(x,y,"Select preset:")
	chosen_preset = display_option_menu(x,y+2,preset_name_list,fore_color='MAGENTA')

	chosen_preset_tuning_list = []
	for preset in PRESETS:
	    if preset['name'] == chosen_preset:
	        chosen_preset_tuning_list = preset['tuning_list']
	        break

	return chosen_preset_tuning_list