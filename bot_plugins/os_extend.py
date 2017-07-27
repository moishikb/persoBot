import os

def execute_dir():
    return os.popen("dir c:\\").read()


def execute__local_dir():
    return os.popen("dir").read()


def get_info2():
    info ='<div class="container"><div class="panel panel-default"><div class="panel-heading">Info about <b>os extend </b> operations</div><div class="panel-body"><table class="table"><thead><tr><th>Function</th><th>Description</th><th>Notes</th></tr></thead><tbody><tr><td>execute__local_dir</td><td>print dir results</td><td>simple output</td></tr><tr><td>execute_dir</td><td></td><td></td></tr></tbody></table></div></div></div>'
    return info