import os

os.system('clear')
fileName = raw_input('Enter a name for the configuration to be created: ')
file = open(fileName, 'w')

file.write("import time\n")
file.write("from pykeyboard import PyKeyboard\n\n")
file.write("kb = PyKeyboard()\n\n")
file.write("def readInput(username, message):\n")

done = False

currentMessage = raw_input("Enter a chat string to search for: ")
file.write("    if(message == \'" + currentMessage + "\'):\n")
file.write("        print(username + \": \" + message)\n")
currentKeyEvent = raw_input("Enter a keyboard event to simulate: ")
file.write("        kb.press_key(\'" + currentKeyEvent + "\')\n")
currentDuration = raw_input("Enter a duration (sec) for this keyboard event: ")
file.write("        time.sleep(" + currentDuration + ")\n")
file.write("        kb.release_key(\'" + currentKeyEvent + "\')\n")
contin = raw_input("Would you like to create another string/event pair? (Y/N): ")
while(contin != 'Y' and contin != 'N'):
    contin = raw_input("Would you like to create another string/event pair? (Y/N): ")
if(contin == 'N'):
    done = True


while(done == False):
    currentMessage = raw_input("Enter a chat string to search for: ")
    file.write("    elif(message == \'" + currentMessage + "\'):\n")
    file.write("        print(username + \": \" + message)\n")
    currentKeyEvent = raw_input("Enter a keyboard event to simulate: ")
    file.write("        kb.press_key(\'" + currentKeyEvent + "\')\n")
    currentDuration = raw_input("Enter a duration (sec) for this keyboard event: ")
    file.write("        time.sleep(" + currentDuration + ")\n")
    file.write("        kb.release_key(\'" + currentKeyEvent + "\')\n")
    contin = raw_input("Would you like to create another string/event pair? (Y/N): ")
    while(contin != 'Y' and contin != 'N'):
        contin = raw_input("Would you like to create another string/event pair? (Y/N): ")
    if(contin == 'N'):
        done = True
