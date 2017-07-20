def say_hello():
    return 'hello, Moshik '

def say_hello2():
    return 'hello, Moshik2 '

functions = {'say_hello': say_hello, 'say_hello2': say_hello2}


def list_of_ops():
    list = '<ul class="list-group">'
    for item in functions:
        list += '<li class="list-group-item">'+item+'</li>'
    list += '</ul>'
    return list


def get_function(function_name):
    return functions[function_name]
