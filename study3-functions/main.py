### FUNCTIONS



'''
In Python, the if __name__ == '__main__': line is used to determine if the current module 
is being run as the main program or if it is being imported as a module by another program.

When a Python file is executed directly as a standalone program, the special variable __name__ is set to '__main__'. 
However, when a file is imported as a module into another program, the value of __name__ is set to the name of the module.

By using the if __name__ == '__main__': condition, you can separate the code that should only run when the module is executed as the main program. 
This allows you to have code that will be executed when the file is run directly, but not when it is imported as a module.
'''


#In the following code, if the module is being run as the main program (i.e., directly executed), 
# it will prompt the user to enter two numbers and then call the calculator function from the imported 
# function module to perform the calculations and display the results. 
# However, if the module is imported as a module by another program, the code 
# inside the if __name__ == '__main__': block will not be executed.

from function import calculator

if __name__ == '__main__' :
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))

    print(calculator(x, y))
