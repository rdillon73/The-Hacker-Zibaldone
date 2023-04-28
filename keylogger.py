# keylogger.py

import time
from pynput import keyboard

# Initialize the logging variables
log = ""
start_time = time.time()

# Define the function to handle key press events
def on_press(key):
    global log, start_time, listener

    try:
        # Get the pressed key as a string
        key_str = key.char
    except AttributeError:
        # Handle special keys like space and enter
        key_str = " " + str(key) + " "

    # Add the pressed key to the log
    log += key_str

    # Calculate the elapsed time and typing speed
    elapsed_time = time.time() - start_time
    speed_factor = len(log) / elapsed_time  

    # Print the current typing speed
    print(f"Current typing speed: {speed_factor:.2f} ")

    # Check if the Escape key was pressed
    if key == keyboard.Key.esc:
        # Stop the listener
        listener.stop()

# Create a keyboard listener and start logging
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Wait for the listener to finish (i.e., the script to be stopped)
listener.join()

# Save the log to a file
with open("key_log.txt", "w") as f:
    f.write(log)
