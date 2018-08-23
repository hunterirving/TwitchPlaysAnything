import time
from pykeyboard import PyKeyboard

kb = PyKeyboard()

def readInput(username, message):
        if(message == 'kill'):
            kb.press_key(asd)
        if(message == "a"):
            print(username + ": " + message)
            kb.press_key('a')
            time.sleep(0.5)
            kb.release_key('a')
        elif(message == 'b'):
            print(username + ": " + message)
            kb.press_key('b')
            time.sleep(0.2)
            kb.release_key('b')
        elif(message == 'c'):
            print(username + ": " + message)
            kb.press_key('c')
            time.sleep(0.2)
            kb.release_key('c')
        elif(message == 'u'):
            print(username + ": " + message)
            kb.press_key('i')
            time.sleep(0.2)
            kb.release_key('i')
        elif(message == 'r'):
            print(username + ": " + message)
            kb.press_key('l')
            time.sleep(0.2)
            kb.release_key('l')
        elif(message == 'd'):
            print(username + ": " + message)
            kb.press_key('k')
            time.sleep(0.2)
            kb.release_key('k')
        elif(message == 'l'):
            print(username + ": " + message)
            kb.press_key('j')
            time.sleep(0.2)
            kb.release_key('j')
        elif(message == 'left'):
            print(username + ": " + message)
            kb.press_key('m')
            time.sleep(0.2)
            kb.release_key('m')
        elif(message == 'right'):
            print(username + ": " + message)
            kb.press_key('r')
            time.sleep(0.2)
            kb.release_key('r')
        elif(message == 'la'):
            print(username + ": " + message)
            kb.press_key('j')
            time.sleep(0.2)
            kb.press_key('a')
            time.sleep(1)
            kb.release_key('a')
            kb.release_key('j')
        elif(message == 'ra'):
            print(username + ": " + message)
            kb.press_key('l')
            time.sleep(0.2)
            kb.press_key('a')
            time.sleep(1)
            kb.release_key('a')
            kb.release_key('l')
        elif(message == 'da'):
            print(username + ": " + message)
            kb.press_key('a')
            kb.press_key('k')
            time.sleep(0.05)
            kb.release_key('k')
            kb.release_key('a')
