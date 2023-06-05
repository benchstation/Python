'''
Create a list that has these values ( 20 , 40 , 30 , 10 , 0 ).
Turn them into a descending list.
Delete position two [2] and show the off value.
Insert the value two (2) into position four (4).
Print the size of the list.
'''

values_list = [20, 40, 30, 10, 0]

# Sort the list in descending order
values_list.sort(reverse=True)
print("Descending list:", values_list)

# Delete element at index 2 and print the deleted value
deleted_value = values_list.pop(2)
print("Deleted value at index 2:", deleted_value)

# Insert the value 2 at index 4
values_list.insert(4, 2)
print("List after inserting value 2 at index 4:", values_list)

# Print the size of the list
size = len(values_list)
print("Size of the list:", size)