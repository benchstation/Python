# Create a program that asks for a grade between 0-10.
# Show a message if the value is invalid and keep prompting until the user enters a valid value.

# To guarantee we don't enter an infinite loop, make the grade variable start with a value beyond the max value (10)
grade = 100 

while grade > 10 or grade < 0:
   grade = int(input("Enter the value for a grade between 0 and 10"))

print("The grade entered was: ", grade)

