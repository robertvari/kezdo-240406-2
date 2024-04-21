add_numbers = lambda a, b : a + b
divide_numbers = lambda a, b : a / b
multiply_numbers = lambda a, b : a * b

add_result = add_numbers(10, 34)
divide_result = divide_numbers(add_result, 5)
multiply_result = multiply_numbers(divide_result, 200)

print(multiply_result)