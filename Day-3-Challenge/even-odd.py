print("--------------Lesson 8 Day 3: Odd or Even -------------------")

# Prompt the user to enter a number and convert the input to an integer
# This value is stored in the variable 'number'
number = int(input("Enter any number! "))

# Check if the number is even by using the modulo operator
if number % 2 == 0:
    # If the result of the modulo operation is 0, the number is even
    print("This is an even number!")
else:
    # If the result is not 0, the number is odd
    print("This is an odd number!")
