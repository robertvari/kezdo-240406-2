#     lib folder      library(namespace)  alias
from my_functions import math_functions as mf

add_result = mf.add_numbers(10, 20)
divide_result = mf.divide_numbers(add_result, 10)
multiply_result = mf.multiply_numbers(divide_result, 10)

print(f"The result is: {multiply_result}")