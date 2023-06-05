# Write an algorithm using a while loop that prompts the user for N ages, the program only counts ages greater than or equal to 18.
# And at the end of the code it should show the number of users who have +18.
# The program must prompt for values until the user enters -1.

"""
# Initializing relevant variables
count = 0  # Variable to keep track of the number of users with age >= 18
min_age = 18  
n = int(input("Enter an age (or -1 to exit): "))

while n != -1:
    if n >= min_age:
        print("User is an adult.")
        count += 1  # Increment the count if age >= 18
    else:
        print("User is a minor.")
    n = int(input("Enter an age (or -1 to exit): "))

print("Number of users who are 18 or older:", count)
"""

# Observation: 
# The above code is fine but it sometimes can result in unwanted behavior
# when the user accidentally presses ENTER and produces an empty string ('') before trying to convert the value into an integer with int().

'''
    The ValueError: invalid literal for int() with base 10: '' error occurs when you try to convert 
    an empty string to an integer using int(). 
    It happens when you press the Enter key without entering any value, which results in an empty string.
    To handle this situation, you can add a condition to check if the input is an empty string before converting it to an integer. 
'''

# So, here's the better way of dealing with the empty string ('') problem: 
count = 0  # Variable to keep track of the number of users with age >= 18
min_age = 18
n = input("Enter an age (or -1 to exit): ")

while n != '-1':
    if n != '' and int(n) >= min_age: # Condition to check if the input is an empty string
        print("User is an adult.")
        count += 1
    elif n != '':
        print("User is a minor.")
    n = input("Enter an age (or -1 to exit): ")

print("Number of users who are 18 or older:", count)

# With this solution, even if the user accidentally presses ENTER, the program will prompt them to enter an age once again without crashing.


### PROFESSOR'S SOLUTION
age, count = 0, 0
while True:
    age = int(input("Enter an age (or a negative value to terminate): "))
    if age < 0:
        break  # Exit the loop if the age is negative
    if age >= 18:
        count += 1

print("Number of users who are 18 or older:", count)

