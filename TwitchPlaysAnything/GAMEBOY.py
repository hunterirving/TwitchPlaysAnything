import time
from pykeyboard import PyKeyboard

kb = PyKeyboard()

def readInput(username, message):
        if(message == 'a'):
            print(username + ": " + message)
            kb.press_key('a')
            time.sleep(0.2)
            kb.release_key('a')
        elif(message == 'b'):
            print(username + ": " + message)
            kb.press_key('b')
            time.sleep(0.2)
            kb.release_key('b')
        elif(message == 'up' or message == 'u'):
            print(username + ": up")
            kb.press_key('u')
            time.sleep(0.2)
            kb.release_key('u')
        elif(message == 'right' or message == 'r'):
            print(username + ": right")
            kb.press_key('r')
            time.sleep(0.2)
            kb.release_key('r')
        elif(message == 'down' or message == 'd'):
            print(username + ": down")
            kb.press_key('d')
            time.sleep(0.2)
            kb.release_key('d')
        elif(message == 'left' or message == 'l'):
            print(username + ": left")
            kb.press_key('l')
            time.sleep(0.2)
            kb.release_key('l')
        elif(message == 'start'):
            print(username + ": " + message)
            kb.press_key('s')
            time.sleep(0.2)
            kb.release_key('s')
        elif(message == 'select'):
            print(username + ": " + message)
            kb.press_key('e')
            time.sleep(0.2)
            kb.release_key('e')
        elif(message == 'save replay' and username == 'pythonchatbot'):
            print(username + ": " + message)
            print("REPLAY SAVED.")
            kb.press_key('p')
            time.sleep(0.2)
            kb.release_key('p')
        elif(message == 'clear screen' and username == 'pythonchatbot'):
            for x in range(0, 50):
                print("\n")
