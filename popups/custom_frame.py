import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class CustomPopup:
    def __init__(self, parent):
        self.parent = parent
        self.kernel_size = None
        self.entered_values = None
        self.entry_grid = None  # Make entry_grid an instance variable

        self.top = tk.Toplevel(parent)
        self.top.title("Custom Options")

        # Entry for the name
        name_label = tk.Label(self.top, text="Name:")
        name_label.grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(self.top)
        self.name_entry.grid(row=0, column=1, pady=5)

        # Entry for the kernel size
        kernel_label = tk.Label(self.top, text="Kernel Size:")
        kernel_label.grid(row=1, column=0, pady=5)
        self.kernel_entry = tk.Entry(self.top)
        self.kernel_entry.grid(row=1, column=1, pady=5)

        # Button to register the entered number and create the grid
        register_button = tk.Button(self.top, text="Register", command=self.register_kernel_size)
        register_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Frame to hold the Entry widgets in a grid
        self.frame = tk.Frame(self.top)
        self.frame.grid(row=3, column=0, columnspan=2, pady=10)

        # OK button to register the entered values in the grid
        ok_button = tk.Button(self.top, text="OK", command=self.ok_button_pressed)
        ok_button.grid(row=4, column=0, columnspan=2, pady=10)

    def register_kernel_size(self):
        try:
            self.kernel_size = int(self.kernel_entry.get())
            if self.kernel_size <= 0:
                raise ValueError("Kernel size must be a positive integer.")

            # Clear the previous widgets in the frame
            for widget in self.frame.winfo_children():
                widget.destroy()

            # Create a grid of Entry widgets based on the kernel size
            self.entry_grid = [[tk.Entry(self.frame, width=5) for _ in range(self.kernel_size)] for _ in range(self.kernel_size)]

            # Display the grid of Entry widgets
            for i in range(self.kernel_size):
                for j in range(self.kernel_size):
                    self.entry_grid[i][j].grid(row=i, column=j)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def ok_button_pressed(self):
        try:
            # Retrieve the entered values from the grid
            self.entered_values = np.zeros((self.kernel_size, self.kernel_size), dtype=float)
            for i in range(self.kernel_size):
                for j in range(self.kernel_size):
                    value_str = self.entry_grid[i][j].get()
                    if value_str:
                        self.entered_values[i][j] = float(value_str)

            print(f"Entered Name: {self.name_entry.get()}")
            print(f"Entered Kernel Size: {self.kernel_size}")
            print("Entered Values:")
            print(self.entered_values)

            # Close the popup
            self.top.destroy()

        except ValueError:
            messagebox.showerror("Error", "Invalid value entered. Please enter valid numbers.")
        except TypeError:
            messagebox.showerror("TypeError", "Please fill values")

# Example usage:
# custom_popup = CustomPopup(root)
# root.wait_window(custom_popup.top)
