

# dang func
def display_decorator(func):

    def wrapper(str):
        # logic trước khi chạy hàm func
        print(f'Log: The function {func.__name__} is executing ...')
        func(str)
        # logic sau khi chạy hàm func
        print('Log: Execution completed.\n')
    return wrapper


def display(str):
    print(str)


display = display_decorator(display)
display('Hello world')


@display_decorator
def say_hello(str):
    print(str)


say_hello('Hello, Donald')


# dang class
class decoclass(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        # logic trước khi gọi hàm f
        print('decorator initialised')
        self.f(*args, **kwargs)
        print('decorator terminated')
        # logic sau khi gọi hàm f


@decoclass
def hello(name):
    print(f'Hello, {name}. Welcome to heaven!')


print(hello('Obama'))

