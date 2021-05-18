a, b = 1, 0
# try:
#     div = a/b
#     print(a, b)
# except:
#     print(f"Division by {b} is not accepted.")


try:
    if a % 2 == 0:
        raise Exception("a is even.")
except Exception as var1:
    print(var1)


# def validate_distance(distance):
#     assert(distance > 6), "Distance must be greater than 6 feet"
# print(validate_distance(5))

try:
    distance = int(input("Enter a distance:"))
    zu = distance/"asd"
    zd = distance/0
    print(distance)
except ValueError:
    print("Value Error: Entered number is not valid.")
except ZeroDivisionError:
    print("The number can't be divided by zero.")
except:
    print("Unknown error.")
else:
    print("Else clause executed if no exception is found.")
finally:
    print("Finally clause executed if exception is found or not found.")
