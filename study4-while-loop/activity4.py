# Make a program that reads a username and its password and does not accept the password equal to the username,
# showing an error message and asking again for the information.

login       = input("Login: ")
password    = input("Password: ")

while login == password:
   print("Password can't be same as login. Enter a new password.")
   # Do the input again
   password = input("Password: ")

print(f"Your login: {login} "
    f"Your password: {password}")
