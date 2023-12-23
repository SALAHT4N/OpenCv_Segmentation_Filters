import tkinter as tk
from tkinter import filedialog
from popups.line_detection_frame import LineDetectionPopup
from popups.edge_detection_frame import EdgeDetectionPopup
from popups.thresholding_frame import ThresholdingPopup
from popups.custom_frame import CustomPopup

class FilterButtonsView:
  def __init__(self, parent, state):
      self.state = state
      self.view = tk.Frame(parent, width=150, bg="lightgray")
      self.view.pack(side=tk.LEFT, fill=tk.Y)
      self.parent = parent

      filters_label = tk.Label(self.view, text="Filters", font=("Helvetica", 10, "bold"), bg="lightgray")
      filters_label.pack(side=tk.TOP, pady=5)

      button_names = ["Point Detection", "Line Detection", "Edge Detection", "LoG", "Thresholding", "Custom"]
      button_handlers = [self.point_detection, self.line_detection, self.edge_detection, self.log_detection,
                           self.thresholding, self.custom_detection]

      for name, handler in zip(button_names, button_handlers):
          button = tk.Button(self.view, text=name, command=handler, width=15)
          button.pack(side=tk.TOP, pady=5)
  def point_detection(self):
      # Add your point detection code here
      pass

  def log_detection(self):
      # Add your LoG (Laplacian of Gaussian) code here
      pass
      
  def line_detection(self):
      line_popup = LineDetectionPopup(self.parent)
      self.parent.wait_window(line_popup.top)
      selected_value = line_popup.selected_value
      if selected_value is not None:
          print(f"Line Detection Option Selected: {selected_value}")
          # Perform line detection with the selected value here

  def edge_detection(self):
      edge_popup = EdgeDetectionPopup(self.parent)
      self.parent.wait_window(edge_popup.top)
      selected_option = edge_popup.selected_option.get()
      if selected_option is not None:
          print(f"Edge Detection Option Selected: {selected_option}")
      # Perform edge detection with the selected option here

  def thresholding(self):
      threshold_popup = ThresholdingPopup(self.parent)
      self.parent.wait_window(threshold_popup.top)
      selected_value = threshold_popup.selected_value
      if selected_value is not None:
          print(f"Thresholding Value Selected: {selected_value}")
          # Perform thresholding with the selected value here

  def custom_detection(self):
          # Open a pop-up window for Custom Detection
      custom_popup = CustomPopup(self.parent)
      self.parent.wait_window(custom_popup.top)
      kernel = custom_popup.entered_values
      print(kernel)
