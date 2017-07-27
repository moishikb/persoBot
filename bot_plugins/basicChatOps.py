from datetime import datetime
import os


def say_hello():
    return 'hello, Moshik '


def what_is_the_time():
    return str(datetime.now())


def task_manager():
    return os.popen(r"C:\Windows\System32\taskmgr.exe").read()

def get_info():
    info ='<div class="container"><div class="panel panel-primary"><div class="panel-heading">Info about <b>Basic Chat Ops </b> operations</div><div class="panel-body"><table class="table"><thead><tr><th>Function</th><th>Description</th><th>Notes</th></tr></thead><tbody><tr><td>say_hello</td><td>Just to say hello to the user </td><td>simple output</td></tr><tr><td>what_is_the_time</td><td>Return the current computer full time and date</td><td>time format</td></tr><tr><td>task_manager</td><td>Open the task manager</td><td></td></tr></tbody></table></div></div></div>'
    return info