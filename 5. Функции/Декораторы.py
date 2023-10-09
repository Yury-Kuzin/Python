def border(size):
    def func_decorator(func):
        def out_func(*args, **kwargs):
            stars = '*' * (len(args[0]) + size)
            return f'{stars}\n{func(*args)}\n{stars}'
        return out_func
    return func_decorator



@border(25)
def hello_name(name):
    return f'Добро пожаловать, {name}'


print(hello_name('Иван'))
