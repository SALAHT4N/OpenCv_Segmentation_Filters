import tkinter as tk
from tkinter import ttk

class EdgeDetectionPopup:
    def __init__(self, parent):
        self.parent = parent
        self.selected_option = None
        self.selected_value = None

        self.top = tk.Toplevel(parent)
        self.top.title("Edge Detection Options")

        options = ["+45", "-45", "Vertical", "Horizontal"]
        self.selected_option = tk.StringVar()
        # self.selected_option.set(options[0])  # Default selection

        for option in options:
            radio_button = ttk.Radiobutton(self.top, text=option, variable=self.selected_option, value=option, style='Dark.TRadiobutton')
            radio_button.pack(anchor=tk.W)

        ok_button = tk.Button(self.top, text="OK", command=self.ok_button_pressed)
        ok_button.pack(pady=10)

    def ok_button_pressed(self):
        self.selected_value = self.selected_option.get()
        self.top.destroy()

# You can add additional methods or modify as needed for edge detection options
