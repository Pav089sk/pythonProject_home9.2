from functools import wraps

def log(filename):
    """Декоратор для логирования функции"""
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
              if filename is not None:
                  with open ('mylog.txt', 'a') as file:
                      file.write(f'{func.__name__}, "ok"')
              else:
                  print(f'{func.__name__}, "ok"')
            except TypeError as a:
                if filename is not None:
                    with open('mylog.txt', 'a') as file:
                        file.write(f'{func.__name__},"type error" {a}, Inputs: {args}, {kwargs}')
                else:
                    print(f'{func.__name__}, {a}, "type error" {a}, Inputs: {args}, {kwargs}')
            result = func(*args, **kwargs)
            return result
        return inner
    return wrapper



@log(filename=None)
def my_function(x, y):
    return x + y

my_function('1', {} )
