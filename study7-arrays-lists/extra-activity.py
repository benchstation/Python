'''
Make a program, with a function that takes an argument.
The function returns the character value 'P', if its argument is positive, and 'N', if its argument is zero or negative.
'''

def check_sign(number):
    if number > 0:
        return 'P'
    else:
        return 'N'

# Test the function
num = float(input("Enter a number: "))
sign = check_sign(num)
print("Sign:", sign)
