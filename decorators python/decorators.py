def decorator_function(function_to_decorate):
    def nested_function(name):
        return name.upper()

    return nested_function

@decorator_function
def hello(name):
    return name

@decorator_function
def hello2(fullname):
    return fullname

print(hello2("Ukakjdsfgsdkkdbfsha"))