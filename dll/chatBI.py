import os
import socket
import json
import re
import datetime
import importlib
import glob
from shutil import copyfile
from inspect import getmembers, isfunction

# ************************************************************
# ******               Local functions:                  *****


def show_my_ip():
    return socket.gethostbyname(socket.gethostname())


def show_my_hostname():
    return socket.gethostname()


def run_command(msg):
    command = str(msg).replace('#', '').replace('run:', '')
    res = os.popen(command).read()
    return '<br>Done<br><pre>' + res + '</pre>'


# ************************************************************
#  ****** mechanism to manage the external bot plugins:  *****

# return list of package names as strings
def list_of_available_packages():
    packages_list = []
    for file in glob.glob("bot_plugins/*.py"):
        if 'init' not in file:
            packages_list.append(str(file).replace('\\', '.').replace('.py', ''))
    return packages_list


def list_of_available_functions_in_package(package_name):
    imported_module = importlib.import_module(package_name)
    functions_list = [o for o in getmembers(imported_module) if isfunction(o[1])]
    return functions_list


def get_list_of_all_functions():
    msg = '<b>List of functions you can ask from me to do<b><hr>'
    packages_list = list_of_available_packages()
    for module in packages_list:
        msg += '<ul class="list-group">'
        msg += '<li class="list-group-item list-group-item-info">' + str(module)+'</li>'
        functions = list_of_available_functions_in_package(module)
        for item in functions:
            msg += '<li class="list-group-item">'+item[0]+'</li>'
        msg += '</ul>'
    return msg


def run_function(func):
    flag = False
    try:
        packages_list = list_of_available_packages()
        for module in packages_list:
            functions = list_of_available_functions_in_package(module)
            if func in str(functions):
                imported_module = importlib.import_module(module)
                mymethod = getattr(imported_module, func)
                msg = mymethod()
                flag = True
                break
        if flag:
            return 'done<br>' + msg
        else:
            return 'Function didnt found in the imported plugins!'
    except:
        return "Problem to run the function"

# ************************************************************
#  ****** mechanism to manage the local knowledge-base:  *****


def get_answer_from_knowledge(msg):
    try:
        file = open(r"dll\bot_knowledge.json", 'r')
        data = json.load(file)
        file.close()
        flag = False
        results = ''
        for item in data:
            p = re.compile('.*'+item.replace(' ','.*')+'.*', re.IGNORECASE)
            if p.match(msg):
                results += str(data[item])
                flag = True
                break
        if not flag:
            results = "Sorry, i'm not familiar with such question, You can teach me by going to the <a href='teach.html'><span class='label label-default'>Teach me<span></a> page."
        return results
    except:
        return "Seems like my knowledge became corrupted, please make sure you didn't miss something!"


def add_new_fac_to_knowledge(question,answer):
    try:
        re.compile(question)
    except re.error:
        return "Error: The question: " + question + " contains invalid regular expression!"
    if question == '#' or  question == '@':
        return "Error: The symbol: " + question + " is used by the system for run functions"
    if len(question) < 2 or len(answer) < 2:
        return "Error: One or more of the inputs are too short to be real input"
    try:

        json_file_path = r"dll\bot_knowledge.json"
        backup_json_file(json_file_path)
        with open(json_file_path) as json_file:
            json_decoded = json.load(json_file)
        json_decoded[question] = answer
        with open(json_file_path, 'w') as json_file:
            json.dump(json_decoded, json_file)
        return "Done"
    except:
        return "Sorry but i failed to add new row to the knowledge-base!"


def backup_json_file(file):
    date = str(datetime.datetime.now())[:18]
    date = date.replace(' ', '_').replace(':', '')
    copyfile(file, file+date)


def get_message(msg):
    decorate = '<div class="panel panel-default"><div class="panel-body">'
    if 'Welcome aboard' in msg:
        decorate = '<div class="alert alert-success">'
    elif 'run:' in msg or msg[0] == '#':
        msg = '<span class="label label-default">Execute</span><br>' + run_command(msg)
    elif 'ip' in msg or 'IP' in msg:
        msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;' + 'Your IP: ' + show_my_ip()
    elif 'machine name' in msg or 'host name' in msg:
        msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;' + 'Your  host name: ' + show_my_hostname()
    elif 'list' in msg and 'action' in msg or 'method' in msg:
        msg = get_list_of_all_functions() + '<div class="alert alert-warning">To invoke one of those actions please use "@" as a prefix before the function name. e.g <strong>@action_name</strong>.</div>'
    elif msg[0] == '@':
        func_name = msg.replace('@','')
        msg = '<span class="label label-warning">Action:</span>&nbsp;&nbsp;' + run_function(func_name)
    else:
        msg = get_answer_from_knowledge(msg)
        if 'Sorry' in msg:
            msg = '<span class="label label-warning">Info</span>&nbsp;&nbsp;' + msg
        else:
            msg = '<span class="label label-info">Info</span>&nbsp;&nbsp;' + msg
    return decorate + msg + '</div></div>'

