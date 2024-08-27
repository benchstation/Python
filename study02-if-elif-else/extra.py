### EXTRA
# This program must prompt the user for some numbers and then perform operations with said numbers
number1 = float(input("Enter the first number:\n"))
number2 = float(input("Enter the second number:\n"))
operation = int(input("Enter the desired operation (1 - Addition, 2 - Subtraction, 3 - Division, 4 - Multiplication):\n"))

if operation == 1:
    result = number1 + number2
    operation_text = "addition"
elif operation == 2:
    result = number1 - number2
    operation_text = "subtraction"
elif operation == 3:
    result = number1 / number2
    operation_text = "division"
elif operation == 4:
    result = number1 * number2
    operation_text = "multiplication"
else:
    print("Invalid operation. Please try again.")
    exit() # to prevent error

print("The result of", operation_text, "between", number1, "and", number2, "is:", result)

