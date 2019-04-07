def decorator_function(function_to_decorate):
    def new_function(a):
        print('executing decorator function')
        return a.upper() 
    return new_function


@decorator_function
def hello(a):
    return a

print(hello('ukasha'))
