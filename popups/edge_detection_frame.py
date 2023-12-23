import tkinter as tk

class EdgeDetectionPopup:
    def __init__(self, parent):
        self.parent = parent
        self.selected_option = None

        self.top = tk.Toplevel(parent)
        self.top.title("Edge Detection Options")

        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])  # Default selection

        for option in options:
            radio_button = tk.Radiobutton(self.top, text=option, variable=self.selected_option, value=option)
            radio_button.pack(anchor=tk.W)

        ok_button = tk.Button(self.top, text="OK", command=self.ok_button_pressed)
        ok_button.pack(pady=10)

    def ok_button_pressed(self):
        self.top.destroy()

# You can add additional methods or modify as needed for edge detection options
