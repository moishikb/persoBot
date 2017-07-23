from datetime import datetime
import os


#--------------     FUNCTIONS      ----------------
# Functions that will be available to the bot, please add your own functions under that line and before the functions dictionary definition

def say_hello():
    return 'hello, Moshik '


def say_hello2():
    return 'hello, Moshik2 '


def what_is_the_time():
    return str(datetime.now())

def execute_dir():
    return os.popen("dir c:\\").read()

#--------------------------------------------------
#-----------     functions dictionary  ------------
#  Add new row here for any new function you are adding to the script
functions = {'say_hello': say_hello,
             'say_hello2': say_hello2,
             'what_is_the_time': what_is_the_time,
             'execute_dir':execute_dir}


#-----------    PACKAGE Mechanism  ----------------


def list_of_ops():
    list = '<ul class="list-group">'
    for item in functions:
        list += '<li class="list-group-item">'+item+'</li>'
    list += '</ul>'
    return list


def get_function(function_name):
    return functions[function_name]
