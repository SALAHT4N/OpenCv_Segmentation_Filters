import tkinter as tk
from tkinter import ttk

class PointDetectionPopup:
    def __init__(self, parent):
        self.parent = parent
        self.threshold_value = None

        self.top = tk.Toplevel(parent)
        self.top.title("Point Detection Options")

        self.threshold_scale = ttk.Scale(self.top, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=self.update_label)
        self.threshold_scale.set(127)  # Default threshold value
        self.threshold_scale.pack(pady=10)

        self.value_label = tk.Label(self.top, text=f"Threshold Value: {int(self.threshold_scale.get())}")
        self.value_label.pack(pady=5)

        ok_button = tk.Button(self.top, text="OK", command=self.ok_button_pressed)
        ok_button.pack(pady=10)

    def update_label(self, value):
        try:
            value_int = int(float(value))
            self.value_label.config(text=f"Threshold Value: {value_int}")
        except ValueError:
            pass  # Handle the error as needed

    def ok_button_pressed(self):
        self.threshold_value = int(self.threshold_scale.get())
        self.top.destroy()

# You can add additional methods or modify as needed for point detection options
