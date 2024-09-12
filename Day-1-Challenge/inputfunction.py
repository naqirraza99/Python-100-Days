# Print a header for the lesson
print("----------------Lesson 3 Day 1-Input Function---------------")

# Prompt the user to enter their name (this input is not stored or used)
input("What is your name?")

# Prompt the user to enter their name again, take the input, and display it immediately
print(input("What is your name?"))

# Prompt the user to enter two numbers, convert the inputs to integers, and calculate their product
num1 = int(input("Enter the 1st Number:"))
num2 = int(input("Enter the 2nd Number"))
print(num1 * num2)  # Print the product of the two numbers

# Concatenate the strings "Naqi" and "Raza", and calculate the length of the resulting string
len_size = len("Naqi" + "Raza")
print()  # Print an empty line for better readability
print("The length of name is", len_size)  # Display the length of the concatenated string

# Prompt the user to enter their name, and print the length of the input string
name_size = input("What is your name?")
print(len(name_size))  # Print the length of the name provided by the user

# Print a message indicating the length of the user's name
print("Your name has a length of", len(name_size))

# Prompt the user to enter another input and print the length of this new input
name_size = input()
print(len(name_size))  # Print the length of the new input

# Prompt the user to enter input again and immediately print the length of this input
print(len(input()))  # Take input from the user and print its length immediately
