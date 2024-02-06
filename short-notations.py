from pynput.keyboard import Key, Listener, Controller
from notations import shortcuts, write_power, coding_char, max_symbols


# The current sequence of keys pressed
current_keys = ""


keyboard = Controller()

typing_on = False


def on_press(key):
    global current_keys, typing_on

    if len(current_keys) > max_symbols:
        current_keys = ""
        typing_on = False
    try:
        # Convert the key to a string and remove quotes
        key_char = str(key).replace("'", "")

        if key_char == coding_char and not typing_on:
            typing_on = True
            current_keys = coding_char

        if typing_on:
            # Add the pressed key to the current sequence
            if len(key_char) == 1:
                current_keys += key_char

                if key_char == coding_char and len(current_keys) > 1:

                    seq = current_keys.replace(coding_char, "")
                    output = ""

                    # special case for '^{number}' case
                    if seq:
                        if seq[0] == "^":
                            output = write_power(seq[1:])
                        else:
                            # Check if the current sequence matches the target sequence
                            for sequence, output in shortcuts.items():
                                if seq == sequence:
                                    if output == "stop":
                                        # stop the listener
                                        return False
                                    break
                            else:
                                output = ""

                    if output:
                        # Backspace to remove the sequence
                        for _ in range(len(current_keys) - 1):
                            keyboard.press(Key.backspace)
                            keyboard.release(Key.backspace)

                        # Type the replacement symbol
                        keyboard.type(output)

                        # Clear the current sequence
                        current_keys = ""
                        typing_on = False

            elif key_char == "Key.backspace":
                # Remove the last key if backspace is pressed
                try:
                    current_keys = current_keys[:-1]
                except IndexError:
                    pass
            else:
                pass

    except AttributeError:
        pass  # Special keys (like space) will not be letters


def on_release(key):
    pass


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
