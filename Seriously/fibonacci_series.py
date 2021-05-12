

def custom_gen(a, b):
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
