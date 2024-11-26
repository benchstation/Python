'''
Create a program that receives 5 values and shows the sum of the values.
After that calculate the average of this list.
'''

# Initialize an empty list
values = []

# Receive 5 values from the user
for _ in range(5):
    value = float(input("Enter a value: "))
    values.append(value)

# Calculate the sum of the values
sum_of_values = sum(values)

# Calculate the average of the values
average = sum_of_values / len(values)

# Print the sum and average
print("Sum of the values:", sum_of_values)
print("Average of the values:", average)
