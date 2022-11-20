import keyboard

#next line writes test@examples.com aftew writing "@ " anywhere on the system
#keyboard.add_abbreviation("@", "test@example.com");

def callback():
    print ("Callback called")

#class Keylogger:
    #def __init__(self):


#keyboard.wait()


keyboard.on_release(callback())
keyboard.wait()


#test = Keylogger()