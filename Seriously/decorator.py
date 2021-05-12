"""
Functions are objects: they can be assigned to the variables and passed to and returned from other function
Function can be defined inside another function
"""


# def decorate_me(func):
#     def inner_func():
#         print("It is now decorated")
#         func()  # none()

#     return inner_func


# @decorate_me
# def ordinary():
#     print("ordinary")
#     return None


# ordinary()


# decorated = decorate_me(ordinary)  # inner_func will be returned
# decorated()


# def sum(a, b):
#     return a+b
# def outer_fun(func):
#     return func
# sum_value = sum
# outer_fun(sum_value)


# def null_decorator(func):
#     def reply():
#         print("Good Moring imksav!")
#         func()
#         return "Returned from reply"
#     return reply


# # @next_decorator
# @null_decorator
# def greet():
#     return "Good Morning Keshav!"


# greet()
# greeting = null_decorator(greet)  # greeting => inner_func
# print(greeting())
"""
def inc(x):
    return x+1


def operate(func, x):
    result = func(x)
    print(x)
    return result


print(operate(inc, 3))
"""
# ==========================================

"""
def print_msg(msg):
    greeting = "Hello,"

    def printer():
        print(greeting, msg)
    printer()


print_msg("Python is awesome.")
"""
"""
# ==========================Main Self Learning Decorators==================
# Method without @


def printer():
    print("Hello World!")


def display_info(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Execution completed")
    return inner


decorated_func = display_info(printer)
decorated_func()
# print("=========================================")

# Method with @


def display_info(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Execution completed")
    return inner


@display_info
def printer():
    print("Hello World!")


printer()
"""
# print("=========================================")

"""
def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Cannot divide by 0!")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b


print(divide(6, 7))
print(divide(5, 0))
"""
# print("=========================================")


def star(func):
    def inner(args):
        print("*" * 10)
        func(args)
        print("*" * 10)
    return inner


def percent(func):
    def inner(args):
        print("%" * 10)
        func(args)
        print("%" * 10)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Decorators completed!")
