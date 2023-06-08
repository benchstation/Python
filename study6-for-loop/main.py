### FOR LOOP

# Repetition with a control variable and a range
 
'''
ABOUT RANGE ---> range()  

In Python, range() is a built-in function that generates a sequence of numbers. 

It is commonly used within for loops to iterate over a specific range of values. 
The range() function can be called with different parameters to define the range of numbers it should generate.

The range() function supports THREE different forms:

range(stop): This form generates a sequence of numbers from 0 to stop - 1. It starts from 0 by default and increments by 1.
Example: range(5) generates the sequence [0, 1, 2, 3, 4].

range(start, stop): This form generates a sequence of numbers from start to stop - 1. It starts from start and increments by 1.
Example: range(2, 7) generates the sequence [2, 3, 4, 5, 6].

range(start, stop, step): This form generates a sequence of numbers from start to stop - 1 with a specified step value. It starts from start and increments by step.
Example: range(1, 10, 2) generates the sequence [1, 3, 5, 7, 9] (which means, every 2 steps)

The range() function returns a range object that represents the sequence of numbers. 
It doesn't generate the entire sequence at once, but rather generates the numbers on-demand as they are needed during iteration. 
This makes it memory-efficient when working with large ranges.

'''

# Syntax:
distance = 4
for variable in range(distance):
    print("Hello world!")
"""
OUTPUT: 
Hello world!
Hello world!
Hello world!
Hello world!
"""

# Example1
for n in range (1, 30) : 
    print("Loop: ", n)


# Example2
amount = int(input('Amount of grades: '))
mean = 0
for i in range (amount):
    grade = float(input(f'What grade {i + 1}: '))
    mean += grade

mean = mean/amount

print(f'Final grade: {mean: .2f}')


# Example3
new_amount = int(input("How many numbers?\n"))

for i in range (new_amount):

    num = int(input("What's the number: "))

    if num <= 0:

        num = 1

        print(num)

    else:

        print(num)

### INCREMENTING
for x in range (0, 100 + 1, +1):
   print(x)

### DECREMENTING
for y in range (100, 0 - 1, -1):
   print(y)


# Loops are different but they can also be used in a similar way. 
# For example, here's how you would do the same thing by using a FOR loop versus using a WHILE loop:
# FOR
for c in range (0, 100 + 1, +1):
  print(c)

# WHILE
c = 0
while (c < 100 + 1):
   print(c)
   c += 1

# Another example showing range()'s START, STOP and STEP paramters
n1 = int(input("Which number do you want to start: "))
n2 = int(input("How much do you want to step? "))
n3 = int(input("Which number do you want to end: "))

for count in range(n1, n3 + 1, n2):
   print(count)


### LOOP FLAGS - SPECIAL KEYWORDS FOR LOOPS (break, pass, continue)
# In Python, 'break', 'pass', and 'continue' are keywords that are used in different contexts to control the flow of execution of a program.

'''
break : 

A break statement is used to break out of the closest loop it is in.

When Python encounters the break keyword, it exits the loop and continues program execution from the point immediately after the loop.

'''

# break example
for i in range(5):
   if i == 3:
       break
   print(i)


'''
pass : 

The pass keyword is used when you need a syntactically valid statement or block of code, but don't want to do anything. 
It's basically a placeholder that does nothing. 

This command is useful in situations where you are writing code where you need to fill in logic later.

'''

# pass example
for i in range(5):
   if i == 3:
       pass
   else:
       print(i)


'''
continue : 

The continue statement is used to skip the rest of the code inside a loop and move on to the next iteration.

When Python encounters a continue keyword, it skips the rest of the loop and continues with the next iteration. 

'''

# continue example
for i in range(5):
   if i == 2:
       continue
   print(i)


### THROWAWAY VARIABLES
# Conventionally represented by the underscore (_). 
for i in range(5):
    print("Hello, World!")

# Would be the same as:
for _ in range(5):
    print("Hello, World!")

# Instead of using a variable name that we won't use for the loop index, we use "_" as a placeholder. 
# It serves as a visual indication that the loop variable is intentionally ignored.