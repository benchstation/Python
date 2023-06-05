### -------------------- ALL ACTIVITIES FROM THIS STUDY START HERE -------------------

# Create a function that accepts 2 variables and returns the multiplication between them.
def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(result)  # OUTPUT: 15

# Create a function that receives a variable and shows it on the screen if it is a multiple of 2.
def even(num):
    # Using the Ternary Operator
    print(f'{num} is a multiple of 2!') if num % 2 == 0 else print(f'{num} is a multiple of 1!')

# Calculator Function
def calculator(num1, num2):
    sum = num1 + num2
    subtraction = num1 - num2
    product = num1 * num2
    division = num1 / num2
    return f'Sum: {sum} Subtraction: {subtraction} Product: {product} Division: {division}'

### -------------------- ALL ACTIVITIES FROM THIS STUDY END HERE -------------------

### CALLING & USING A FUNCTION + RETURN
# output_variable = funcao(input_variable)

# (1)
def function1(a, b):
  	return a + b

print("First example:", function1(5, 2))

# (2)
def function2(a, b):
  	print("Second example:", a + b)
"""
Note: 
    If you don't define a return value to a function and you later call it, 
    it will return undefined.

    And in this case, nothing will be printed because this function isn't 
    being called anywhere.
"""

# (3)
def function3(a, b):
  	return a + b

new = function3(5, 2)
print("Third example:", new)

# (4)
def function4(a, b):
    new_value = a + b
    return new_value

result = function4(5, 2)
print("Fourth example:", result)