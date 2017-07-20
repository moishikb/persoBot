import os
import socket
import json
import re
from plugins.basicChatOps import list_of_ops, get_function


def show_my_ip():
    return socket.gethostbyname(socket.gethostname())


def show_my_hostname():
    return socket.gethostname()


def run_command(msg):
    command = str(msg).replace('run:', '')
    res = os.popen(command).read()
    return 'Done, dude<br><pre>' + res + '</pre>'


def run_function(func):
    return func()


def get_answer_from_knowledge(msg):
    file = open(r"dll\bot_knowledge.json", 'r')
    data = json.load(file)
    file.close()
    flag = False
    results = ''
    for item in data:
        p = re.compile(item, re.IGNORECASE)
        if p.match(msg):
            results += str(data[item])
            flag = True
    if not flag:
        results = "Sorry, i'm not familiar with such question"
    return results


def get_message(msg):
    if 'Welcome aboard' in msg:
        msg = msg
    elif 'run:' in msg:
        msg = run_command(msg)
    elif 'ip' in msg or 'IP' in msg:
        msg = 'Your IP: ' + show_my_ip()
    elif 'machine name' in msg:
        msg = 'Your  host name: ' + show_my_hostname()
    elif 'list' in msg and 'actions' in msg:
        msg = 'You can work with those operations:<br>' + list_of_ops()
    elif msg[0] == '@':
        func_name = msg.replace('@','')
        msg = run_function(get_function(func_name))
    else:
        msg = get_answer_from_knowledge(msg)

    return '<pre>' + msg + '</pre>'

