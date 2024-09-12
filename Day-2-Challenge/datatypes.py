# Print a header for the lesson
print("--------------------Lesson 4 Day 1: Data Types-------------------- ")

# Prompt the user to enter a number and display its type
num = int(input("Enter a number: "))  # Convert input to integer and store in 'num'
print("The type of the entered number is:", type(num))  # Print the type of 'num'
print()

# Print a header for the program to add two-digit numbers
print("Program to add two digit numbers:")
print()

# Prompt the user to enter a two-digit number as a string
two_digit_number = input("Enter a two-digit number: ")  # Store the input as a string

# Extract the first and second digits from the string and convert them to integers
first_digit = int(two_digit_number[0])  # Convert the first character to integer
second_digit = int(two_digit_number[1])  # Convert the second character to integer

# Calculate the sum of the two digits
sum_digits = first_digit + second_digit  # Rename 'sum' to 'sum_digits' to avoid confusion with the built-in sum() function

# Print the result
print("The sum of the digits is:", sum_digits)
