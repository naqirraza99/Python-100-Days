# Print a header for the lesson
print("------------------------Lesson 1 Day 2: Life in a Week---------------------------")

# Prompt the user to enter their age and display it
age = input("Enter your age: ")
print(f"Your age is {age}")

# Calculate the remaining years of life assuming a life expectancy of 90 years
life_in_years = 90 - int(age)
print(f"Your remaining life in years: {life_in_years}")

# Calculate the remaining life in weeks (52 weeks per year)
life_in_weeks = 52 * life_in_years
print("You have", life_in_weeks, "weeks left.")
