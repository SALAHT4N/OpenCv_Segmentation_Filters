import tkinter as tk

class LineDetectionPopup:
    def __init__(self, parent):
        self.parent = parent
        self.selected_value = None

        self.top = tk.Toplevel(parent)
        self.top.title("Line Detection Options")

        options = ["+45", "-45", "Vertical", "Horizontal"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])  # Default selection

        for option in options:
            radio_button = tk.Radiobutton(self.top, text=option, variable=self.selected_option, value=option, width=30)
            radio_button.pack(anchor=tk.W)

        ok_button = tk.Button(self.top, text="OK", command=self.ok_button_pressed)
        ok_button.pack(pady=10)

    def ok_button_pressed(self):
        self.selected_value = self.selected_option.get()
        self.top.destroy()
