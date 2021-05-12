"""
def add(num1, num2):
    ' ' ' this is doc string ' ' '
    return num1+num2


sum = add(15, 16)
print(sum)
#  to print the doc string of any function write as belo
print(add.__doc__)  # function_name.__doc__

"""

"""
def mul_fun(num1, num2):
    sum = num1+num2
    diff = num1 - num2
    return sum, diff


calculate = mul_fun(3, 8)
print(calculate)  # (11,-5) which is tuple
# to unpack the tuple follow the below code
calc_sum, calc_diff = mul_fun(3, 8)
print(calc_sum, calc_diff)  # print side by side
print(calc_sum)
print(calc_diff)
"""
# objects, variables and functions
"""
1. Positional Argument or non-default parameter (sum, total, data)
2. Keyword parameter or default parameter (sum=50, total=1522, user="name")
3. Keyword only parameter (*agrs)
4. Var-Keyword parameter (**kwargs)

    - Keyword args must follow the positional args
    sum(4,n1=15)
"""

"""
def show_args_type(sum, total, count=0, args=[], *agrs, **kwargs):
    print(sum)
    print(total)
    print(count)
    print(args)  # gives as list
    print(kwargs)  # gives dict
    pass


show_args_type(100, 2050, 7, ["while", "for"], "Keshav",
               "Ram", "Shyam", "imksav", address="Btl", year=2021)
"""

"""
def welcome(user, attempt=1):
    if(attempt == 1):
        print("Welcome "+user+"! This is your first login.")
    else:
        print("Welcome back "+user+"!")


welcome("Keshav")
welcome("imksav", 2)

print("========================================")
"""
"""
def user_data(user, group,  role="Python Developer", id=1):
    print(id)
    print(user)
    print(group)
    print(role)


user_data("imksav", "Admin")
user_data(user="Keshav", group="Field Member", role="Technical Support", id=5)

"""
"""
# Arbitary args list


def books(*categories):
    print(type(categories))
    print(categories)
    for b in categories:
        print(b)


books("Technical", "Programming", "Fiction")
"""
"""
Functions are first class citizens
    - Functions can be objects
    - Functions can be stored in a data structure
    - Functions can be nested
    - Functions can be used as variables
"""
"""

def func(name):
    return "Hello " + name.upper() + "!"

"""
"""
great = func
print(great("imksav"))
print("===================")
"""
"""
del func
print(great("imksav"))  # object is not deleted
func("keshav")  # function gets deleted
"""
"""
funcs = [func, str.title, str.lower, str.upper]
for f in funcs:
    # iterating in the list and implementing functions for above
    print(f("imksav"))
"""
"""
# function inside function


def get_great_message(current_time):
    def morning(name):
        return "Good Morning " + name+"!"

    def afternoon(name):
        return "Good Afternoon "+name+"!"
    if current_time < 12:
        return morning
    else:
        return afternoon


greet_message = get_great_message(6)
print(greet_message("imksav"))
"""
"""
# lamda functions


def sqr(x):
    return (x**2)

print(sqr)
def sq(x):
    return x**2


print(sq(4))

"""
"""
#  Filter, Maps, Reduce functions.......


# def even(x): return x % 2 == 0


# # filter(function, iterable)
# print(list(filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
def even(x):
    return x % 2 == 0


filtered_data = filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(filtered_data))
for f in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    even(f)
# use of lamda


# def odd(y): return y % 2 != 0
def odd(t): return t % 2 != 0


filtered_odd_data = filter(odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(filtered_odd_data))

def natural(n): return n > 0


filtered_natural_numbers = filter(natural, [0, 1, 2, 3, 4, 5, -5, -9])
print(list(filtered_natural_numbers))
"""
# Use of Maps to be learnt, reduce,
"""
Functions:
    Higher order function
    Closures
"""
"""
Non-local variables
Non-local
"""

"""
def outer_func():
    a = "local"

    def inner_func():
        nonlocal a
        a = "I am not local"
        print("inner func: ", a)

    inner_func()
    print("outer func:", a)


outer_func()
"""
"""
# Closure is a function that remembers its reation env (enclosing scope)


def greet(msg):
    def print_message(new_msg):
        #  the variable is accessible from the inner function as well

        print(msg)
        print(new_msg)
    return print_message


message = greet("Hello World")
message("Second message")
message("New Message")
"""
"""
Closure is a function that remembers its creation env (enclosing scope)
    - there must be a nested function
    - the nested function must refer to a value defined in the enclosing function
    - the enclosing function must return the nested function
"""

# what I understand is here of closure:
# but many more confusion.........


def greet(msg):
    def reply_greet(reply):
        print(id(msg))
        print(id(reply))
    return reply_greet


message = greet("Good Morning Keshav!")
print(id(message))
message("Good Morning imksav!")
print(id(message))
