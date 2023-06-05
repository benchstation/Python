'''
 (\(\ 
 ( -.-) 
 o_(")(")
'''
### 02 CONDITIONALS: if, elif, else
"""
If statements use a different flow of execution in comparison to the sequential execution.

In the 'sequential execution flow' each of the lines of code were executed from top to bottom and always respecting this order.

The conditional flow of execution is based on decision. The “if”, “elif”, “else” statements will allow a piece of code to be executed or not.

Python still brings one more detail: what defines a block of commands or a sequence of commands is the indentation.

This is not common in C-derived languages such as C++, Java, JavaScript.

Working with indentation has the advantage of making the code aesthetically cleaner, but it requires a lot of attention from the programmer

It's important to take extra attention to the number of spaces used in indentation.

"""
# Assignment Operators
"""
Use = to assign a value to a variable
a = 1
b = 2
c = 3
Use == in a conditional. "Is equal to"
"""

# a += b    ----> a = a + b
# a -= b    ----> a = a - b
# a *= b    ----> a = a * b
# a /= b    ----> a = a / b
# a %= b    ----> a = a % b
# a **= b   ----> a = a ** b
# a //= b   ----> a = a // b

var = 1 # var takes the value 1
print(var) # OUTPUT: 1

var += 5 # It's the same as saying : var = a + 5
print(var) # OUTPUT: 6

var -= 2 # var gets -2 to the previous value -> var is 4 now
print(var)

# Relational operators

# >	    ------  More than...			    
# <	    ------  Less than...				
# >=    ------  More or equal to...    
# <=	------	Less or equal to...
# ==	------	Is equal to...	

# Logical operators (Logic Gates)
"""
There are actually seven basic logic gates: 
    AND, OR, XOR, NOT, NAND, NOR, and XNOR
But the three most used are the ones below.
"""
# and
# not	------	Not equal to... ('not' can also bre written as !=)
# or
	

# ASCII art showing the logical and relational operators in Python along with their priority or precedence, from highest to lowest:
'''
In Python, operators with higher precedence are evaluated first, 
and operators with the same precedence are evaluated from left to right. 
Parentheses can be used to change the order of evaluation.

+------------+-------------------------------+------------+
|  Operator  |         Description           | Precedence |
+------------+-------------------------------+------------+
|    ()      |       Parentheses             |  Highest   |
|    **      |       Exponentiation          |            |
|  *, /, %   |  Multiplication, Division,    |            |
|            |         Modulo                |            |
|    +, -    |    Addition, Subtraction      |            |
|   <, <=,   | Relational Operators          |            |
|   >, >=,   | (less than, less than or      |            |
|   ==, !=   | equal to, greater than,       |            |
|            |  greater than or equal to,    |            |
|            |          equal to,            |            |
|            |         not equal to          |            |
|    not     |         Logical NOT           |            |
|    and     |         Logical AND           |            |
|    or      |         Logical OR            |   Lowest   |
+------------+-------------------------------+------------+

'''
# Here's an example that demonstrates the precedence of these operators:
result = 2 + 3 * 4 - (5 ** 2) / 10
print(result)  # Output: 14.5


### STRUCTURE OF DECISION

# A < condition > is any operation that returns boolean values, i.e. true or false 
# In Python it is shown as True or False

condition1 = True
condition2 = False
a = 2
b = 3
if (condition1) :
    a + b
elif (condition2) :
    a * b
else :
    a / b

"""
Writing it like this will throw an error "IndentationError: expected an indented block"

if (condition1) :
a + b
elif (condition2) :
a * b
else :
a / b

This is probably how you would write the same block of statement in the C Family:
if (condition1) {
a + b
} else if (condition2) {
a * b
} else {
a / b
}
"""

### TESTING CONDITIONS

x = int(input("Enter a magical number :\n"))
if x > 2 :
   print("Your number is higher than 2.")
elif x == 2 :
   print("Your number is equal 2.")
else :
   print("Your number is less than 2.")


### PASS - null statement
"""
The keyword "pass" should be used whenever the program syntactically requests
to fill in a gap, e.g. as the definition of a function: after the def line there has to be some content.
It produces a null statement, that is, an empty value.
"""
num = int(input("Enter a number higher than 5:\n"))
if num > 5 :
   pass # does nothing
else :
 print("The number entered is less than or equal 5.")


### TERNARY OPERATOR 
# In Python, the ternary operator is a concise way to express a conditional statement in a single line. 
# It allows assigning a value to a variable based on a boolean expression.

# SYNTAX: 
# (if command) if (condition) else (else command)
# value_if_true if condition else value_if_false
# The condition is evaluated first. If the condition is true, the value_if_true is assigned to the variable. Otherwise, the value_if_false is assigned.

# Example1
number = int(input("Enter a number:\n"))
print("The number is higher than 2.") if number > 2 else print("The number is less than or equal 2.")

# Example2
age = 25
status = "Adult" if age >= 18 else "Minor"
print(status)  # OUTPUT: Adult

""" 
This is how you would do it in the C programming language:

#include <stdio.h>
void main()
{  
(condition) ? <command>   :  <command>    ; 
}
"""

