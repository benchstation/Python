# Find the largest and smallest number from a series of numbers supplied by the user via the keyboard. 
# The program must prompt for values until the user enters -1. (Using while and conditionals)

n = int(input("Enter a number: "))
# Variable to store the given numbers if they're higher than the highest
highest = n
# Variable to store the given numbers if they're lower than the lowest
lowest = n
while n != -1:
   n = int(input("Enter a number: "))
   if n > highest and n != -1:
       highest = n
   if n < lowest and n != -1:
       lowest = n
print("Highest: ", highest)
print("Lowest: ", lowest)


