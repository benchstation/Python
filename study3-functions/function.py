# Ternary Operator
def even(num):
    print(f'{num} is a multiple of 2!') if num % 2 == 0 else print(f'{num} is a multiple of 1!')

# Calculator Function
def calculator(num1, num2):
    sum = num1 + num2
    subtraction = num1 - num2
    product = num1 * num2
    division = num1 / num2
    return f'Sum: {sum} Subtraction: {subtraction} Product: {product} Division: {division}'