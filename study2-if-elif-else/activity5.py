# Create a variation of the previous program, but with the following additional requirements:
# Calculate a weighted average: Weight of Grade 1 is 1, Weight of Grade 2 is 1.5, and Weight of Grade 3 is 2.
# Instead of showing whether the student passed or failed based on the weighted average show a grade of SR, II, MI, MM, MS or SS,
# according to the weighted average and using the following scale:
"""
SR -    0
II - <  2
MI - <  5
MM - <  7
MS - <  9
SS - >= 9
"""

grade1 = float(input("Grade 1:\n"))
grade2 = float(input("Grade 2:\n"))
grade3 = float(input("Grade 3:\n"))

# Validate the grades
if not (0 <= grade1 <= 10) or not (0 <= grade2 <= 10) or not (0 <= grade3 <= 10):
    print("Invalid grade. Grades must be between 0 and 10.")
    exit()

# Adding the weights
'''
The division by 4.5 is required to normalize the weighted average to a scale of 0 to 10.

In this program, we are using weights of 1, 1.5, and 2 for the three grades. 
The sum of these weights is 4.5 (1 + 1.5 + 2 = 4.5). 
By dividing the sum of the weighted grades by 4.5, we ensure that the resulting weighted average 
falls within the range of 0 to 10, which is consistent with the grading system.
'''
grade1 *= 1
grade2 *= 1.5
grade3 *= 2
sum = grade1 + grade2 + grade3
# sum = grade1 *1 + grade2 *1.5 + grade3 * 2

# Calculating the weighted mean + printing it on the screen
average = sum / 4.5
formatted_average = "{:.2f}".format(average)
print("Final grade is:", formatted_average)

if average == 0  :
   print("SR")
elif average < 0:
   exit("Negative numbers are invalid.")
elif average < 2 :
   print("II")
elif average < 5 :
   print("MI")
elif average < 7:
   print('MM')
elif average < 9:
   print("MS")
elif average >= 9 and average <= 10:
   print("SS")

