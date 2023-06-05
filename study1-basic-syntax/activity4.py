# Make a program that receives two float values: one for height and one for weight, to calculate Body Mass Index (BMI).
# Finally show the result (with up to two decimal places)

# BMI = Weight / Height^2

#           Input				    	            Output

#       Weight  :  70				 	         BMI : 25.71
#       Height : 1.65				


print("This program will help you calculture your BMI - Body Mass Index.")
weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))
BMI = weight / (height**2)
print(f"Your BMI is: {BMI: .2f}")
