import os

def execute_dir():
    return os.popen("dir c:\\").read()


def execute__local_dir():
    return os.popen("dir").read()