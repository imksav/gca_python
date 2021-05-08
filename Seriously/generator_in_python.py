"""
Generator in Python
=> Any generator is also an iterator but not vice versa
==> Generator allows you to write iterators in an elegant syntax
=> It avoid writing class with __iter__(), __next__()

Creating Generators in Python
Yield --> It also returns the value but is slightly different than return statement

"""

"""
def duplicator(val):
    while True:
        yield val
        val+1  # now val starts from here in next time


duplicates = duplicator(5)
for duplicate in duplicates:
    print(duplicate)
"""

"""
def my_duplicator(val):
    yield val
    yield val
    yield val


my_gen = my_duplicator(5)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# practice
lists = [1, 2, 3, 4]
l = iter(lists)
print(lists)
print(l)
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#
"""

"""
def duplicator(val, max_repeats):
    count = 0
    while True:
        if count < max_repeats:
            count += 1
            yield val
        else:
            return


duplicates = duplicator(5, 3)
for duplicate in duplicates:
    print(duplicate)
"""


def custom_gen(a, b):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


n1 = int(input("Enter first number of a series:"))
n2 = int(input("Enter second number of a series:"))
t = int(input("Enter how many numbers of series you want to print:"))
fibo = custom_gen(n1, n2)
count = 1
while count <= t:
    count += 1
    print(next(fibo))
