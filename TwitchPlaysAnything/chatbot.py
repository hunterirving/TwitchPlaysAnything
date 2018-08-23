import sys
sys.dont_write_bytecode = True
import re
import socket
import time
from pykeyboard import PyKeyboard
import cfg
import os.path 

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

inputModule = raw_input("Which configuration file would you like to use? ")
while(not os.path.isfile(inputModule)):
    inputModule = raw_input("Which configuration file would you like to use? ")
inputModuleName = inputModule

inputModule = __import__(inputModule.replace('.py', ''))
os.system('clear') #os.system('cls') on windows

print("Welcome to the chat. Now playing " + (inputModuleName.replace('.py', '')) + ".")

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        message = CHAT_MSG.sub("", response)
        message = message[:-2]
        inputModule.readInput(username, message)
