print("-----------------BMI Version 3.0-----------------------")
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to calculate BMI and display the result
def calculate_bmi():
    try:
        # Get height and weight from the user input
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            result = f"Your BMI is {bmi:.2f}, you are underweight."
        elif 18.5 <= bmi < 25:
            result = f"Your BMI is {bmi:.2f}, you have a normal weight."
        elif 25 <= bmi < 30:
            result = f"Your BMI is {bmi:.2f}, you are slightly overweight."
        elif 30 <= bmi < 35:
            result = f"Your BMI is {bmi:.2f}, you are obese."
        else:
            result = f"Your BMI is {bmi:.2f}, you are clinically obese."
        
        # Display result in a message box
        messagebox.showinfo("BMI Result", result)
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Input Error", "Please enter valid numbers for height and weight.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.configure(bg='#f0f8ff')  # Light blue background

# Create a frame for better layout
frame = tk.Frame(root, bg='#e6e6fa', padx=20, pady=20)
frame.pack(padx=10, pady=10, fill='both', expand=True)

# Create and place labels and entries for height and weight
tk.Label(frame, text="Enter your height in meters (e.g., 1.55):", bg='#e6e6fa', font=('Helvetica', 12)).pack(pady=5)
height_entry = tk.Entry(frame, font=('Helvetica', 12), borderwidth=2, relief="solid")
height_entry.pack(pady=5)

tk.Label(frame, text="Enter your weight in kilograms (e.g., 72):", bg='#e6e6fa', font=('Helvetica', 12)).pack(pady=5)
weight_entry = tk.Entry(frame, font=('Helvetica', 12), borderwidth=2, relief="solid")
weight_entry.pack(pady=5)

# Create and place the Calculate button
calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=20)

# Style the button
style = ttk.Style()
style.configure("TButton",
                background="#4caf50",  # Green background
                foreground="white",    # White text
                font=('Helvetica', 12, 'bold'))

# Apply a specific style to the button
calculate_button.configure(style="TButton")

# Run the GUI event loop
root.mainloop()



  