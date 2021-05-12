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


def print_msg(msg):
    greeting = "Hello,"

    def printer():
        print(greeting, msg)
    printer()


print_msg("Python is awesome.")
