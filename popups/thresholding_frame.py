import tkinter as tk
from tkinter import ttk

class ThresholdingPopup:
    def __init__(self, parent):
        self.parent = parent
        self.selected_value = None

        self.top = tk.Toplevel(parent)
        self.top.title("Thresholding Options")

        # Create a scale (trackbar) for selecting the threshold value
        self.threshold_scale = ttk.Scale(self.top, from_=0, to=255, orient=tk.HORIZONTAL, length=200, command=self.update_label)
        self.threshold_scale.set(127)  # Default threshold value
        self.threshold_scale.pack(pady=10)

        # Label to display the current value
        self.value_label = tk.Label(self.top, text=f"Current Value: {int(self.threshold_scale.get())}")
        self.value_label.pack(pady=5)

        # Labels to indicate the min and max values
        min_label = tk.Label(self.top, text="0")
        max_label = tk.Label(self.top, text="255")
        min_label.pack(side=tk.LEFT, padx=10)
        max_label.pack(side=tk.RIGHT, padx=10)

        ok_button = tk.Button(self.top, text="OK", command=self.ok_button_pressed)
        ok_button.pack(pady=10)

    def update_label(self, value):
        self.value_label.config(text=f"Current Value: { int(float(value))}")

    def ok_button_pressed(self):
        self.selected_value = int(self.threshold_scale.get())
        self.top.destroy()

# You can add additional methods or modify as needed for thresholding options
