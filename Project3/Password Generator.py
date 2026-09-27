import tkinter as tk
from tkinter import messagebox
import random
import string


# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x450")
window.resizable(False, False)


# Heading
heading = tk.Label(
    window,
    text="PASSWORD GENERATOR",
    font=("Arial", 24, "bold")
)
heading.pack(pady=25)


# Password length label
length_label = tk.Label(
    window,
    text="Enter Password Length:",
    font=("Arial", 15)
)
length_label.pack(pady=5)


# Password length input
length_entry = tk.Entry(
    window,
    font=("Arial", 16),
    width=10,
    justify="center"
)
length_entry.insert(0, "12")
length_entry.pack(pady=10)


# Generated password display
password_entry = tk.Entry(
    window,
    font=("Arial", 18),
    width=30,
    justify="center"
)
password_entry.pack(pady=20)


# Generate password
def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Warning",
                "Password length should be at least 4."
            )
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


# Copy password
def copy_password():

    password = password_entry.get()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied successfully!"
        )
    else:
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )


# Clear password
def clear_password():

    password_entry.delete(0, tk.END)


# Buttons
tk.Button(
    window,
    text="GENERATE PASSWORD",
    font=("Arial", 14),
    width=22,
    height=2,
    command=generate_password
).pack(pady=10)


tk.Button(
    window,
    text="COPY PASSWORD",
    font=("Arial", 14),
    width=22,
    height=2,
    command=copy_password
).pack(pady=5)


tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 14),
    width=22,
    height=2,
    command=clear_password
).pack(pady=5)


# Start application
window.mainloop()