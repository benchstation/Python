### CHECKING IF A NUMBER IS ODD OR EVEN
# If the number, when divided by 2, produces a remainder of 0, it means it's an even number.
# If that condition is not true, it means it's an odd number.
num = int(input("Enter an integer number: "))
if num % 2 == 0 :
   print("The number is even.\n")
else :
   print("The number is odd.\n")

"""
a = 3
if a % 2 == 1:
    print('The number is ODD \n')
elif a % 2 == 0:
    print('The number is EVEN \n')
else:
    print('Invalid number')
"""