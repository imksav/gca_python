# """
def add(num1, num2):
    ' ' ' this is doc string ' ' '
    return num1+num2


sum = add(15, 16)
print(sum)
#  to print the doc string of any function write as belo
print(add.__doc__)  # function_name.__doc__

# """

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
