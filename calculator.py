import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        birth_date = datetime(int(year_var.get()), int(month_var.get()), int(day_var.get()))
        today = datetime.today()
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_months = today.month - birth_date.month - (today.day < birth_date.day)
        if age_months < 0:
            age_years -= 1
            age_months += 12
        age_days = (today - birth_date).days % 30
        result_label.config(text=f"Age: {age_years} years, {age_months} months, and {age_days} days")
        scrolled_text.insert(tk.END, f"Birthdate: {birth_date.strftime('%d %B %Y')}\n")
        scrolled_text.insert(tk.END, f"Age: {age_years} years, {age_months} months, and {age_days} days\n\n")
    except ValueError as e:
        messagebox.showerror("Error", "Please enter the date correctly.")

# Create the main application window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("500x600")  # Set the size of the window
root.configure(bg="orange")  # Change background color

# Create and configure fonts
label_font = ("Arial", 14)
input_font = ("Arial", 12, "bold")

# Title label
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 20, "bold", "underline"), bg="orange", fg="black")
title_label.pack(pady=20)

# Instructions label
instructions_label = tk.Label(root, text="Enter your birthdate below:", font=label_font, bg="#FFCC80", fg="black")
instructions_label.pack(pady=10)

# Frame for date input
date_frame = tk.Frame(root, bg="#FFCC80")
date_frame.pack(pady=10)

# Day spinbox
day_label = tk.Label(date_frame, text="Day", font=label_font, bg="#FFCC80", fg="black")
day_label.grid(row=0, column=0, padx=10, pady=10)
day_var = tk.StringVar()
day_spinbox = tk.Spinbox(date_frame, from_=1, to=31, textvariable=day_var, font=input_font, width=5)
day_spinbox.grid(row=1, column=0, padx=10, pady=10)

# Month combo box
month_label = tk.Label(date_frame, text="Month", font=label_font, bg="#FFCC80", fg="black")
month_label.grid(row=0, column=1, padx=10, pady=10)
month_var = tk.StringVar()
month_combobox = ttk.Combobox(date_frame, textvariable=month_var, values=[str(i) for i in range(1, 13)], font=input_font, width=5)
month_combobox.grid(row=1, column=1, padx=10, pady=10)

# Year spinbox
year_label = tk.Label(date_frame, text="Year", font=label_font, bg="#FFCC80", fg="black")
year_label.grid(row=0, column=2, padx=10, pady=10)
year_var = tk.StringVar()
year_spinbox = tk.Spinbox(date_frame, from_=1950, to=datetime.now().year, textvariable=year_var, font=input_font, width=8)
year_spinbox.grid(row=1, column=2, padx=10, pady=10)

# Calculate age button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age, font=label_font, bg="#FF5733", fg="white")
calculate_button.pack(pady=20)

# Birthdate label
birthdate_label = tk.Label(root, text="Birthdate:", font=label_font, bg="#FFCC80", fg="black")
birthdate_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=label_font, bg="#FFCC80", fg="black")
result_label.pack(pady=10)

# Scrolled text widget
scrolled_text = scrolledtext.ScrolledText(root, width=50, height=20, font=("Arial", 12), wrap=tk.WORD)
scrolled_text.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
