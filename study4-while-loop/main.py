### WHILE LOOP

# Repetition strategy with check at Start

# Syntax: 
condition = True
while (condition) :
    # Do something
    break # You need to establish a way of breaking out from the loop otherwise it will be stuck in an infinite loop

i = 0
print("Example of while loop:")
while i <= 10 :
    print("Loop \n", i)
    i += 1 # i = i + 1
print("End of loop \n")


'''
ASCII illustration for the LOOP WHILE:

    ┌──────────────┐
    │ Enter while  │
    │    loop      │
    └───────┬──────┘
            │
      Test expression
     ┌──────┴───────┐
     │      │       │
   False    │      True
     │      │       │
┌────┘      │       └─────┐
│           │             │
│        Statements       │
│           │             │
│           └─────────────┘
│
│
│
Exit while loop
'''

# Using While loop together with user input
looping = 's'
while looping == 's' or looping == 'S':
   looping = input("Do you wish to continue? (s/n)? ")
print("End of loop")


### EXTRA: Using print(end=" ")
'''
Normally, when you use print() to write values to the screen using LOOPS they'll appear one below the other.
But by using print(, end=" ") you can print these values next to each other.
Very convenient!
'''
# Printing numbers on separate lines
for number in range(1, 21):
    print(number)

# Printing numbers next to each other
for number in range(1, 21):
    print(number, end=" ")    

