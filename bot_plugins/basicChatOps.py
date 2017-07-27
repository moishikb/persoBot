from datetime import datetime
import os


def say_hello():
    return 'hello, Moshik '


def what_is_the_time():
    return str(datetime.now())


def task_manager():
    return os.popen(r"C:\Windows\System32\taskmgr.exe").read()

