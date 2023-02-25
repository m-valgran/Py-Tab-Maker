# Pynput
from pynput import keyboard

# Handler for released key
key_released = None
def on_release(key):
    global key_released
    key_released = key
    return False

# Waits for a key to be released and returns it
def listen_key_release():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
        global key_released
        return key_released