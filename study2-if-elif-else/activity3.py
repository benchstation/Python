# Make a program that returns the time that is typed and greets according to the time.
# 0 <= dawn < 6
# 6 <= morning < 12
# 12 <= afternoon < 18
# 18 <= evening <= 23


# Input 1: Time: 5      Output 1: It is now 5 o'clock. Good Morning.
# Input 2: Time: 7      Output 2: It is now 7 o'clock. Good morning.
# Input 3: Time: 1pm    Output 3: It is now 1pm. Good afternoon.
# Input 4: Time: 23     Output 3: It is now 23 hours. Goodnight.


hour = int(input("What hour is it? (0-23): "))

if hour < 0 or hour > 23:
    print("The time is invalid! It must be in this format: (0-23)")
elif hour >= 0 and hour < 6:
    print("It is", hour, "hour(s). Good dawn.")
elif hour >= 6 and hour < 12:
    print("It is", hour, "hour(s). Good morning.")
elif hour >= 12 and hour < 18:
    print("It is", hour, "hour(s). Good afternoon.")
elif hour >= 18 and hour <= 23:
    print("It is", hour, "hour(s). Good evening.")



# Another way

time_input = input("Enter the time following this format: (HH:MM): ")
hour, minute = time_input.split(":")
hour = int(hour)
minute = int(minute)


print("Hour: ", hour)
print("Minute: ", minute)
print("")
if 0 <= hour < 6 :
   print(f"{hour}:{minute} --> Good Dawn")
elif 6 <= hour < 12:
   print(f"{hour}:{minute} --> Good Morning")
elif 12 <= hour < 18:
   print(f"{hour}:{minute} --> Good Afternoon")
elif 18 <= hour <= 24:
   print(f"{hour}:{minute} --> Good Evening")
else:
   print(f"The following time --> {hour}:{minute} does not exist.")
