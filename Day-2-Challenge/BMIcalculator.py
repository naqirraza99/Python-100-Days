# print("-------------------BMI Calculator-----------------")
# height=float(input("Enter your Height"))
# weight=float(input("Enter your Weight"))
# BMI_calculate=int(weight / (height * height))
# print("Your BMI Index is:",BMI_calculate)
#
# if(BMI_calculate<18):
#     print("You are underweight!")
# elif(18.5 <= BMI_calculate < 24.9):
#     print("You are normal weight!")
# elif(25 <= BMI_calculate < 29.9):
#     print("You are overweight!")
# else:
#     print("You are obesed!")
#
#
#
import tkinter as tk
from tkinter import messagebox


# Function to calculate BMI and show results
def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Input Error", "Height and Weight must be positive values.")
            return

        bmi = weight / (height * height)
        bmi_rounded = round(bmi, 2)

        # Display the BMI value
        bmi_label.config(text=f"Your BMI Index is: {bmi_rounded}")

        # Determine weight category
        if bmi < 18:
            category = "You are underweight!"
        elif 18.5 <= bmi < 24.9:
            category = "You are normal weight!"
        elif 25 <= bmi < 29.9:
            category = "You are overweight!"
        else:
            category = "You are obese!"

        # Display the weight category
        category_label.config(text=category)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for Height and Weight.")


# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place labels, entries, and button
tk.Label(root, text="Enter your Height (in meters):").grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your Weight (in kilograms):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

bmi_label = tk.Label(root, text="Your BMI Index is: ")
bmi_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

category_label = tk.Label(root, text="")
category_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()

