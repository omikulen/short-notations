from pynput.keyboard import Key, Listener, Controller
from notations import shortcuts, write_power, coding_char, max_symbols


# The current sequence of keys pressed
input_sequence = ""


keyboard = Controller()

# regime of checking the sequence
typing_on = False


def on_press(key):
    global input_sequence, typing_on

    if len(input_sequence) > max_symbols:
        input_sequence = ""

    # typing is always turned off if the sequence is cleared by any means
    if input_sequence == "":
        typing_on = False

    try:
        # Convert the key to a string and remove quotes
        key_char = str(key).replace("'", "")

        # FIRST encounter of the coding character
        if key_char == coding_char and not typing_on:
            typing_on = True

        if typing_on:
            # Add the pressed key to the current sequence
            if len(key_char) == 1:
                input_sequence += key_char

                # try to convert "~...~" into something meaningful
                # if not, the second ~ is just treated as a regular character
                if key_char == coding_char and len(input_sequence) > 1:

                    # remove all ~ from the sequence
                    seq = input_sequence.replace(coding_char, "")
                    output = ""

                    # special treatment of the power '^{number}' case
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
                        for _ in range(len(input_sequence)):
                            keyboard.press(Key.backspace)
                            keyboard.release(Key.backspace)

                        # Type the replacement symbol
                        keyboard.type(output)

                        # Clear the current sequence
                        input_sequence = ""

            # backspace
            elif key_char == "Key.backspace":
                # Remove the last key if backspace is pressed
                try:
                    input_sequence = input_sequence[:-1]
                except IndexError:
                    pass
            # ignore space, shift, ctrl, etc.
            else:
                pass

    except AttributeError:
        pass


def on_release(key):
    pass


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
