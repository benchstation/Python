'''
Create a program that reads 5 numbers and put them in a list.
Also make the sum of the first and third values.
After that, this program will rearrange the list in numerical order.
Once again, make the sum of the first and third values.
At the end show the result on the screen.
'''

# Initialize an empty list
numbers = []

# Read 5 numbers from the user and add them to the list
for _ in range(5):
   number = int(input("Enter a number: "))
   numbers.append(number)
print("Current state of the list (after FOR): ", numbers)

# Calculate the sum of the first and third values
sum_of_values = numbers[0] + numbers[2]
print("Sum of the first and third values (before SORT): ", sum_of_values)
# Rearrange the list in numerical order
numbers.sort()
sum_of_values = numbers[0] + numbers[2]
# Print the resulting list, sum of values, and rearranged list
print("Rearranged list:", numbers)
print("Sum of the first and third values (after SORT):", sum_of_values)

