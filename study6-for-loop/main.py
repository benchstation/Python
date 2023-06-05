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

Uma instrução break é usada para interromper o loop mais próximo em que está inserido. 

Quando o Python encontra a palavra-chave break, ele sai do loop e continua a execução do programa a partir do ponto imediatamente após o loop.

'''

# break example
for i in range(5):
   if i == 3:
       break
   print(i)


'''
pass : 

Uma instrução break é usada para interromper o loop mais próximo em que está inserido. 

Quando o Python encontra a palavra-chave break, ele sai do loop e continua a execução do programa a partir do ponto imediatamente após o loop.

'''
# pass example
for i in range(5):
   if i == 3:
       pass
   else:
       print(i)


'''
continue : 

A instrução continue é usada para pular o restante do código dentro de um loop e avançar para a próxima iteração. 

Quando o Python encontra uma palavra-chave continue, ele ignora o restante do loop e continua com a próxima iteração. 
'''

# continue example
for i in range(5):
   if i == 2:
       continue
   print(i)


