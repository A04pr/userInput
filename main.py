
# This simple program is designed to get user input, check if one of those inputs is in the correct data type, and to print the information gathered. 
print("Hello! I'd like to know more about you")

# User input for variables
name = input('Please enter your first name: ')
n = input('Please enter your favorite number: ')
color = input('Please enter your favorite color: ')

# Try/except to ensure the user has entered a number in integer form (1, 2, 3... etc) and not string (one, two, three... etc)
try:
    number = int(n)
    print("Hello", name, "your favorite color is:", color, "and your favorite number is:", number + ". Thanks for taking the time to chat!")
except:
    print("Please enter a number")
