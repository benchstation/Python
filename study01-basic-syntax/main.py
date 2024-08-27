### About Python
'''
> Interpretive language
> Easy to debug
> Reads code line by line, top to bottom
> Speed: Slow
> Dynamic Type: Doesn't depend on type declarations
> Simpler syntax
> Easy to learn
> Good for linking across languages and platforms
> Open source
> Supports Object-Oriented Programming (OOP)
> Large built-in library
> GUI programming support
> Integrated
'''

### 01 BASIC SYNTAX

# Printing on the console
print("Hello World!")
print("This sentence uses a\nline break")
print("\tThis sentence uses TAB")

# Tips
print("")       # To skip a line
print("\n")     # "ENTER" after executing
print("\t")     # "TAB" after executing

# A commentary is ignored text
'''
a
multiline
comment
note: That's a different way of commenting
one that you don't need to use "#"
however, it's not exactly a comment
this comment is actually a unused string
'''

### VALUES AND TYPES
"""
8                   ---> Integer
2.0                 ---> Floating-point number
"Hello, World!"     ---> String
"""

# Declaring variables
a = 3
b = 8

# Adding variables and printing them
print("The sum result is:", a + b)

# Booleans
c = True

# If statement
if c:
    print("This statement runs because the condition is true")

# ATTENTION: 
# In Python, the print() function does not support assignment operations within its parentheses
# So an operation like print(v += 5) is invalid in Python
# To do something equivalent, you should do it like this:
v = 5
v += 5 # Increment the value of v by 5
print(v) # OUTPUT: 10

### STRINGS

# Both of these are strings
# You use quotation marks ("" or '') to declare strings
str1 = "5"
str2 = 'Hiya'

# Concatenating strings
# Python automatically adds a space in concatenation 
# It also adds a line break after the last character
print(str1,str2) # OUTPUT: 5 4 
# "Adding" strings together 
# This places one character besides another, without adding space
print(str1 + str2) # OUTPUT: 54 

### USER INPUT
# ATTENTION>> input() always converts the value to a string, 
# it expects receiving a string and also returns a string

name = input("Enter your name:\n")
print('Nice to meet you,', name, "!")

'''
The output will always be returned as a string
To avoid it, you will need to convert the data type
This is a process called "type casting"
In Python, the int() and float() functions can be used to do this conversion
They convert a string into a int if you use int(), or a float if you use float()
Note that the string must be a number character to be converted into int or float
Otherwise, the function will raise a ''ValueError''
It's not possible to directly convert the string "hello" to an integer because 
it does not represent a valid numeric value
'''
example_num = int(input("Enter a integer number.\n"))
print("Your number is", example_num, "and when added to 5, it equals:", example_num + 5)

print("Type a random number and press enter. Then, repeat it one more time: ")
f = input(' Value 1 : ')
g = input(" Value 2 : ")

print(f, g)
print(f + g)
print(float(f) + int(g))
print(int(f)+ float(g))

# Using int() and float() functions to convert data types
x = 3.5
y = 6.8
print(int(x) + float(y)) # OUTPUT: 9.8
z = .3
print(float(z)) # OUTPUT: 0.3

# Printing variable data type (nice for debugging)
print(type ('Hello world')) # OUTPUT: <class 'str'>
print(type (5.3)) # OUTPUT: <class 'float'>
print(type (9)) # OUTPUT: <class 'int'>
print(type (True)) # OUTPUT <class 'bool'>

### EMPTY VALUE : None ---> The absence of a value or the lack of a return value
empty_variable = None

# Printing an empty value (or "None")
# var = int(input())
# print (var) # Output will be what was typed in the input

### IMPORTING A MODULE (external python file)
# example module: utils.py
import utils
print(utils.f()) # OUTPUT: foo
utils.f_value = 'bar'
print(utils.f()) # OUTPUT: bar

### ASCII TABLE
# The ord() functions convert a character into its equivalent number in the ASCII table
g_char = 'g'
print("The value of " + g_char + " in the ASCII table is:", ord(g_char)) # OUTPUT: the value of g in the ASCII table is 103
# chr() does the opposite of ord(). It's used to get a character based on its number in the ASCII table
print(chr(65)) # OUTPUT: A
print(chr(120)) # OUTPUT: x
# It is also possible to perform operations
print(chr(ord('S') + 1)) # OUTPUT: T

### COLORING TEXT IN THE CONSOLE
'''
Unfortunately this code does not work in vscode terminal
to color the text in the vscode console, it is necessary to download a library called "COLORAMA"
to install it, use the command 'pip install colorama' and then try the code below.

print("\033[30mThis text is in black.\033[0m")
print("\033[31mThis text is in red.\033[0m")
print("\033[32mThis text is in green.\033[0m")
print("\033[33mThis text is in yellow.\033[0m")
print("\033[34mThis text is in blue.\033[0m")
print("\033[35mThis text is in purple.\033[0m")
print("\033[36mThis text is in cyan.\033[0m")
print("\033[37mThis text is in white.\033[0m")
'''

### ARITHMETIC OPERATORS
"""
Use = to assign a value to a variable
a = 1
b = 2
c = 3

+   ---> returns the addition operation between the left and right value
-   --->  returns the suubtraction operation between the left and right value
*   --->  returns the multiplication operation between the left and right value
/   --->  returns the division operation between the left and right value
%   ---> returns the remainder between the left and right value
**  ---> returns the exponentiation between the left and right value
//  ---> returns the smallest integer that divides the expression

"""
# ( x % y )     ----> Module. Returns the remainder of a division
# ( x ** y )    ----> Exponentiation. Equivalent to "^" in other languages
# ( x // y )    ----> Returns the smallest integer that divides the expression

# Examples
v = 10
w = 3

print(v + w) # OUTPUT: 13
print(v - w) # OUTPUT: 7
print(v * w) # OUTPUT: 30
print(v / w) # OUTPUT: 3.3333...
print(v % w) # OUTPUT: 1
print(v ** w) # OUTPUT: 1000
print(v // w) # OUTPUT: 3

# More examples
xx = 3.5
yy = 6.8

print(float(xx) + int(yy))
#9.5
print(int(xx) + int(yy))
#9
print(str(xx) + str(int(yy)) )
#3.56
print(xx,yy)
#3.5 6.8
print(str(int(yy))*int(xx)+str(xx))

### STRING TEMPLATING

grade = 1
grade_max = 5

# WAY 1:
# Using the '%' operator (like in the C language)
# This type of string formatting is known as "printf-style"
# It involves using '%' as a placeholder inside the string and after closing the string,
# bring it up again this time adding the values that should replace this operator.
print("The grade entered is: %.2f which is less than: %.2f" % (grade, grade_max))               # %

# WAY 2: 
# Using 'f-strings'
# This is a newer formatting strategy introduced in Python 3.6.
# Lets you embed expressions directly in curly braces { } within strings.
# Preceded by the prefix 'f'
print(f"The grade entered is: {grade:.2f} which is less than: {grade_max:.2f}")                # f-string

# WAY 3:
# Using the .format() method
# This method allows for more flexibility.
# Involves creating a template string using curly braces { } which act as placeholders
# Then call the .format() method on the string, passing the values to be replaced as method arguments.
print("The grade entered is: {:.2f} which is less than: {}".format(grade, grade_max))          # .format

# WAY 4:
# Using concatenation
# To separate strings, use commas
# (unlike most languages where you separate strings from variables using the "+" operator)
print("The grade entered is:", grade, "which is less than:", grade_max)                         # concatenation

### ASCII TABLE
# Link for complete version: https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm

# 10 ----> line break
# 32 ----> blank space
# A ----> 65
# B ----> 66
# C ----> 67
# D ----> 68
# E ----> 69
# F ----> 70
# G ----> 71
# H ----> 72
# I ----> 73
# J ----> 74
# K ----> 75
# L ----> 76
# M ----> 77
# N ----> 78
# O ----> 79
# P ----> 80
# Q ----> 81
# R ----> 82
# S ----> 83
# T ----> 84
# U ----> 85
# V ----> 86
# W ----> 87
# X ----> 88
# Y ----> 89 
# Z ----> 90
# [ ----> 91
# \ ----> 92
# ] ----> 93
# ^ ----> 94
# _ ----> 95
# ` ----> 96
# a ----> 97
# b ----> 98
# c ----> 99
# d ----> 100
# e ----> 101
# f ----> 102
# g ----> 103
# h ----> 104
# i ----> 105
# j ----> 106
# k ----> 107
# l ----> 108
# m ----> 109
# n ----> 110
# o ----> 111
# p ----> 112
# q ----> 113
# r ----> 114
# s ----> 115
# t ----> 116
# u ----> 117
# v ----> 118
# w ----> 119
# x ----> 120
# y ----> 121
# z ----> 122
