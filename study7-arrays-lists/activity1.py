'''
Create a program that receives 5 values and then: 
    - Add these values in the list;
    - Show the amount of stored values;
    - Print the list.
'''

# Create an empty list
values_list = []

# Receive 5 values from the user and add them to the list
for _ in range(5):
    value = input("Enter a value: ")
    values_list.append(value)

# Show the amount of stored values
num_values = len(values_list)
print("Number of stored values:", num_values)

# Print the list
print("List of values:", values_list)

