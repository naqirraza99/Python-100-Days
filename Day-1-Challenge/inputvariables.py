# Print a header for the lesson
print("--------------------Lesson 4 Day 1: Input Variables-------------------- ")
print()

# Program to swap two numbers
print("Program to swap Two numbers:")

# Prompt the user to enter the first number and convert it to an integer
a = int(input("Enter first number: "))

# Prompt the user to enter the second number and convert it to an integer
b = int(input("Enter second number: "))

# Swap the values of 'a' and 'b'
c = a  # Temporarily store the value of 'a' in 'c'
a = b  # Assign the value of 'b' to 'a'
b = c  # Assign the value of 'c' (original 'a') to 'b'

# Print the swapped values
print("After Swapping:")
print("a:", a)
print("b:", b)
