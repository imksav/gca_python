"""
Iterator:
Iterator protocols:
     It must implement __iter__() method
     It must implement __next__() method
"""
"""
iter()
next()
names = ['John', 'Jane']
name = iter(names)
print(next(name))
print(next(name))
print(next(name))
"""
"""
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
"""
"""
family = ["bhandari", "shrestha", "gaire", "acharya"]
family_iter = iter(family)
while True:
    try:
        family = next(family_iter)
        print(family)
    except StopIteration:
        break
"""


class Duplicator:
    def __init__(self, val, max_repeat):
        self.val = val
        self.max_repeats = max_repeat
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_repeats:
            self.count += 1
            return self.val
        raise StopIteration


duplicates = Duplicator(5, 10)
# for duplicate in duplicates:
#     print(duplicate)
duplicate_iterator = iter(duplicates)
print(next(duplicate_iterator))
