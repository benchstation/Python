# Develop a math times table generator, capable of generating the table of any integer between 1 and 10. 
# The user must inform which number to see the table.

# USING WHILE:
number = int(input("Enter a number to generate its times table (1-10): "))

if 1 <= number <= 10:
    i = 0
    while i <= 10:
        result = number * i
        print(f"{number} x {i} = {result}")
        i += 1
else:
    print("Invalid input. Please enter a number between 1 and 10.")

"""
USING FOR: 

number = int(input("Enter a number to generate its times table (1-10): "))

# Validate the input number
if number < 1 or number > 10:
    print("Invalid number. Please enter a number between 1 and 10.")
else:
    print(f"Times table for {number}:")

    # Generate and print the times table
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
"""

# Observation: About range()
'''
    In Python, the range(start, stop) function generates a sequence of numbers from start up to, but not including, stop.

    In the context of generating the times table, we want to iterate from 1 to 10 inclusively. Therefore, we use range(1, 11) instead of range(0, 10).

    By using range(1, 11), the loop will iterate from 1 to 10, executing the block of code for each iteration. 
    
    Meanwhile if we used range(0, 10), the loop would iterate from 0 to 9, and we would miss generating the times table for the number multiplied by 10.

'''