# Replaces a character in a string at a given position
def replace_at(text, replace_index, replace_with):
    return text[:replace_index] + replace_with + text[replace_index+1:]