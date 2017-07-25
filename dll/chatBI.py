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
    return '<br>Done<br><pre>' + res + '</pre>'


def run_function(func):
    return func()


def get_answer_from_knowledge(msg):
    try:
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
    except:
        return "Seems like my knowledge became corrupted, please make sure you didn't miss something!"


def add_new_fac_to_knowledge(question,answer):
    try:
        json_file_path = r"dll\bot_knowledge.json"
        with open(json_file_path) as json_file:
            json_decoded = json.load(json_file)
        json_decoded[question] = answer
        with open(json_file_path, 'w') as json_file:
            json.dump(json_decoded, json_file)
        return "Done"
    except:
        return "Sorry but i failed to add new row to the knowledge-base!"


def get_message(msg):
    decorate = '<div class="well well-sm">'
    if 'Welcome aboard' in msg:
        decorate = '<div class="alert alert-success">'
    elif 'run:' in msg:
        msg = '<span class="label label-default">Execute</span><br>' + run_command(msg)
    elif 'ip' in msg or 'IP' in msg:
        msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;' + 'Your IP: ' + show_my_ip()
    elif 'machine name' in msg or 'host name' in msg:
        msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;' + 'Your  host name: ' + show_my_hostname()
    elif 'list' in msg and 'action' in msg or 'method' in msg:
        msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;You can work with those operations:<br><br>' + list_of_ops() + '<div class="alert alert-success">To invoke one of those actions please use "@" as a prefix before the function name. e.g <strong>@action_name</strong>.</div>'
    elif msg[0] == '@':
        func_name = msg.replace('@','')
        msg = '<span class="label label-warning">Action</span>&nbsp;&nbsp;' + run_function(get_function(func_name))
    else:
        msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;' + get_answer_from_knowledge(msg)
    return decorate + msg + '</div>'

