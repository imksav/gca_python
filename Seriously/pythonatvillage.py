"""
Iterator:
Iterator protocols:
     It must implement __iter__() method
     It must implement __next__() method
"""
# """
iter()
next()
names = ['John', 'Jane']
name = iter(names)
print(next(name))
print(next(name))
print(next(name))
# """
# """
sizes = [15, 22, 36]
for size in sizes:
    print(size)

print("================")

size_iter = iter(sizes)
while True:
    try:
        size = next(size_iter)
        print(size)
    except StopIteration:
        break
# """

family = ["bhandari", "shrestha", "gaire", "acharya"]
family_iter = iter(family)
while True:
    try:
        family = next(family_iter)
        print(family)
    except StopIteration:
        break
