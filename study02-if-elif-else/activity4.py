# INSTRUCTIONS:
# Create a program that receives three grades from 0 to 10 (do the validations to accept only this range)
# Then calculate the arithmetic average and then show the alternating average and also if the student passed or failed
# The school accepts grades 7+ for approval
# Pay attention to the indentation
'''
n1 = float(input("1st Grade: "))
if n1 < 0 or n1 > 10:
    print ("Invalid")
else:
    n2 = float(input("2nd Grade: "))
    if n2 < 0 or n2 > 10:
        print ("Invalid")
    else:
          n3 = float(input("3rd Grade: "))
          ...
'''

print("In this hypothetical school, those who have a final average of 7 or more will pass.")
print("You'll be prompted to enter three grades to check if you passed or not.")

average = 0

n1 = float(input("Enter your first grade (0-10): "))
if n1 < 0 or n1 > 10:
  print("Your 1st grade ((%.1f)) is invalid!"% (n1))
  exit()

n2 = float(input("Enter your 2nd grade (0-10): "))
if n2 < 0 or n2 > 10 :
  print("Your 2nd grade ((%.1f))is invalid!"% (n2))
  exit()

n3 = float(input("Enter your 3rd grade (0-10): "))
if n3 < 0 or  n3 > 10:
  print("Your 3rd grade ((%.1f)) is invalid!\n"%(n3))
  exit()

average = n1 + n2 + n3
average /= 3

if average >= 7 and average <= 10 :
   print("\nYou passed with a grade of: ((%.2f)), congratulations." % (average))

elif average < 0 or average > 10 :
   print("\nThe entered values are invalid, please try again.")
else:
   print("\nYou failed with a grade of: ((%.3f)), please try again next semester."%(average))

