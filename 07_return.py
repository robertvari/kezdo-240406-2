def add_numbers(a, b) -> int:
    return a + b

def divide_numbers(a, b) -> float:
    return a / b

def multiply_numbers(a, b) -> int:
    return a * b

def print_result(result):
    print(f"The result is: {result}")

add_result = add_numbers(10, 34)
divide_result = divide_numbers(add_result, 5)
multiply_result = multiply_numbers(divide_result, 200)

print_result(multiply_result)
