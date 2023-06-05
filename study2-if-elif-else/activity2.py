# Develop a program that takes two integers and returns the one with the higher value.
 
# Input: 2 , 3             Output: Higher value: 3
# Input: 4 , 3             Output: Higher value: 4
# Input: 5 , 5             Output: Higher value: 5

print("This program compares two integers and tells you which one is the greater.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Comparing both numbers and saving the highest in a variable
if num1 > num2:
    higher = num1
elif num2 > num1:
    higher = num2
else:
    print("Both numbers are equal.")
    exit()

print("The higher value is:", higher)



print("Let's try again...")

# Using try and except to deal with the possibility of the input receiving a float instead of an integer
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. You should only enter integer numbers.")
    exit()

if num1 > num2:
    higher = num1
elif num2 > num1:
    higher = num2
else:
    print("Both numbers are equal.")
    exit()

print("The higher value is:", higher)
