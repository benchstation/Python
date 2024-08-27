'''
Create a function that receives a list of numbers stored in ascending order, and two values (lower limit and upper limit),
and display the sublist whose elements are greater than or equal to the lower bound and less than or equal to the upper bound.

Example:

initial_list = [12, 14, 15, 16, 18, 20, 24, 26, 28, 32, 34, 38]
lower_boundary = 13
upper_boundary = 26
displayed_list = [14, 15, 16, 18, 20, 24, 26]
'''

def display_sublist(numbers, lower_boundary, upper_boundary):
    # Initialize an empty list to store the displayed sublist
    displayed_list = []

    # Iterate through each number in the input list
    for number in numbers:
        # Check if the number is within the lower and upper boundaries
        if lower_boundary <= number <= upper_boundary:
            # Add the number to the displayed list
            displayed_list.append(number)

    # Return the displayed sublist
    return displayed_list


# Example usage
initial_list = [12, 14, 15, 16, 18, 20, 24, 26, 28, 32, 34, 38]
lower_boundary = 13
upper_boundary = 26
result = display_sublist(initial_list, lower_boundary, upper_boundary)
print(result) # OUTPUT: [14, 15, 16, 18, 20, 24, 26] 
# Values that are below the lower_boundary such as 12 or values above the upper_boundary such as 28, 32, 34 and 38 didn't show up.
