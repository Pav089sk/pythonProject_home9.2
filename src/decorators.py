from functools import wraps

def log(filename):
    """Декоратор для логирования функции"""
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
              result = func(*args, **kwargs)
              if filename is not None:
                  with open ('mylog.txt', 'a') as file:
                      file.write(f'{func.__name__}, "ok"')
              else:
                  print(f'{func.__name__}, "ok"')
              return result
            except TypeError as a:
                if filename is not None:
                    with open('mylog.txt', 'a') as file:
                        file.write(f'{func.__name__},"TypeError" {a}, Inputs: {args}, {kwargs}')
                else:
                    print(f'{func.__name__}, "TypeError" {a}, Inputs: {args}, {kwargs}')
                raise a
        return inner
    return wrapper



@log(filename='mylog.txt')
def my_function(x, y):
    return x + y

my_function(1, 2)
