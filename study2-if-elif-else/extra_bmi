# Same as activity3 from study1, but with a small improvement using if-elif-else

"""
+--------------+----------------------+
|     BMI      |   Weight Status      |
+--------------+----------------------+
|   <= 16.9    | Very Underweight     |
| 17.0 - 18.0  | Underweight          |
| 18.5 - 24.0  | Healthy              |
| 25.0 - 29.0  | Overweight           |
| 30.0 - 34.0  | Obesity Level 1      |
|   < 40.0     | Obesity Level 2      |
|   >= 40.0    | Obesity Level 3      |
+--------------+----------------------+

"""

print("This program will help you calculate your BMI - Body Mass Index.")
try:
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers. Please try again.")
    else:
        BMI = weight / (height ** 2)
        print(f"Your BMI is: {BMI:.2f}")
    # OBS: Attention to the indentation. 
    # If the following block of code started 
    #^-- here, it would throw an error: "NameError: name 'BMI' is not defined"
        if BMI <= 16.9:
            print("Your weight status is Very Underweight.")
        elif BMI <= 18.4:
            print("Your weight status is Underweight.")
        elif BMI <= 24.9:
            print("Your weight status is Healthy.")
        elif BMI <= 29.9:
            print("Your weight status is Overweight.")
        elif BMI <= 34.9:
            print("Your weight status is Obesity Level 1.")
        elif BMI < 40.0:
            print("Your weight status is Obesity Level 2.")
        elif BMI >= 40.0:
            print("Your weight status is Obesity Level 3.")
        # else:
        #     print("The entered weight is invalid. Please try again.")

except ValueError:
    print("The entered weight is invalid. Please try again.")