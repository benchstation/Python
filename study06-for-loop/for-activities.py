# (1) Create a program to print a count from 0 to 100 in steps of 10 (Use For).

for i in range(0, 101, 10):
    print(i)

# (2) Create a program that reads 5 numbers and reports the sum and average of the numbers.
# Using WHILE
count = 0
total = 0

while count < 5:
    number = float(input("Enter a number: "))
    total += number
    count += 1

average = total / 5

print("Sum:", total)
print("Average:", average)

# Using FOR
total = 0

for _ in range(5):
    number = float(input("Enter a number: "))
    total += number

average = total / 5

print("Sum:", total)
print("Average:", average)

# (3) Create a program that asks the user for a set of 10 real values and outputs the average of the 10 numbers. (using only FOR)
total = 0

for i in range(10):
    number = float(input("Enter a number: "))
    total += number

average = total / 10

print("Average:", average)

# (4) Create a program that receives N integers, and all numbers less than or equal to 0 become 1. (using only FOR)
'''
+-------+---------+
| Input | Output  |
+-------+---------+
|   2   |    2    |
|   3   |    3    |
|   4   |    4    |
|   1   |    1    |
|   0   |    1    |
|  -1   |    1    |
+-------+---------+
'''
n = int(input("Enter the number of integers: "))
sum_numbers = 0

for i in range(n):
    number = int(input("Enter an integer: "))
    if number <= 0:
        number = 1
    sum_numbers += number

average = sum_numbers / n
print("Average of the numbers:", average)
