### Activity 2

# Create a program that receives a name and a number and prints the name the number of times marked by the number:

# Welcome to a Python program, [ name ] and multiply the name


#        Example Input				    	    Example Output
 
#       What's the name : name 				 	Welcome to a Python program, [ name ] 
#    	How many times :  4					    name name name name

name = input("What's your name?\n")
num = int(input("Tell me a magic number...\n"))
for i in range(num):
    print(f"Welcome to a Python program, {name}!")



print("Now, let's try it again..!")



### More advanced alternative using try and except
new_name = input("What's your name?\n")
try:
    new_num = int(input("Tell me a magic number...\n"))
    if new_num <= 0:
        print("Magic number should be a positive integer.")
    else:
        for i in range(new_num):
            print(f"Welcome to a Python program, {new_name}!")
except ValueError:
    print("Invalid magic number. Please enter a numeric value.")

