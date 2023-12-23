import tkinter as tk
import numpy as np
from popups.line_detection_frame import LineDetectionPopup
from popups.edge_detection_frame import EdgeDetectionPopup
from popups.thresholding_frame import ThresholdingPopup
from popups.custom_frame import CustomPopup
from popups.point_detection_frame import PointDetectionPopup

class FilterButtonsView:
  def __init__(self, parent, image_app_mediator, state, opencv_helper):
      self.image_app_mediator = image_app_mediator
      self.view = tk.Frame(parent, width=150, bg="lightgray")
      self.view.pack(side=tk.LEFT, fill=tk.Y)
      self.parent = parent
      self.opencv_helper = opencv_helper
      self.state = state

      filters_label = tk.Label(self.view, text="Filters", font=("Helvetica", 10, "bold"), bg="lightgray")
      filters_label.pack(side=tk.TOP, pady=5)

      button_names = ["Point Detection", "Line Detection", "Edge Detection", "LoG", "Thresholding", "Custom"]
      button_handlers = [self.point_detection, self.line_detection, self.edge_detection, self.log_detection,
                           self.thresholding, self.custom_detection]

      for name, handler in zip(button_names, button_handlers):
          button = tk.Button(self.view, text=name, command=handler, width=15)
          button.pack(side=tk.TOP, pady=5)
  def update_state(self, filter_name, enhanced):
      self.state.add_filter(filter_name)
      self.state.add_image(enhanced)
      self.state.set_current_image(enhanced)

  def point_detection(self):
      point_popup = PointDetectionPopup(self.parent)
      self.parent.wait_window(point_popup.top)
      point_kernel = np.array(
          [
              [-1, -1, -1],
              [-1,  8, -1],
              [-1, -1, -1]
          ]
        ) 
      threshold = point_popup.threshold_value
      
      enhanced = self.opencv_helper.apply_filter(self.state.current_image, point_kernel)
      self.opencv_helper.remove_response_lower_than_threshold(self.state.current_image, enhanced, threshold)
      
      self.update_state("point detection", enhanced)
      self.image_app_mediator.notify(self.state.current_image, "set_image")

  def log_detection(self):
      log_kernel = np.array(
          [
              [0,0,-1,0,0],
              [0,-1,-2,-1,0],
              [-1,-2,16,-2,-1],
              [0,-1,-2,-1,0],
              [0,0,-1,0,0],
          ]
      )
      enhanced = self.opencv_helper.apply_filter(self.state.current_image, log_kernel)
      self.update_state("Laplacian of Gaussian", enhanced)
      self.image_app_mediator.notify(self.state.current_image, "set_image")
      
  def line_detection(self):
      line_popup = LineDetectionPopup(self.parent)
      self.parent.wait_window(line_popup.top)
      selected_value = line_popup.selected_value
      if selected_value is not None:
          kernel = None
          if selected_value == "+45":
              kernel = np.array([
                  [-1,-1,2],
                  [-1,2,-1],
                  [2,-1,-1]
              ])
          elif selected_value == "-45":
            kernel = np.array([
                  [2,-1,-1],
                  [-1,2,-1],
                  [-1,-1,2]
              ])
          elif selected_value == "Vertical":
            kernel = np.array([
                    [-1,2,-1],
                    [-1,2,-1],
                    [-1,2,-1]
                ])
          else:
              kernel = np.array([
                  [-1,-1,-1],
                  [2,2,2],
                  [-1,-1,-1]
              ])
          enhanced = self.opencv_helper.apply_filter(self.state.current_image, kernel)
          self.update_state(f"{selected_value} line detection", enhanced)
          self.image_app_mediator.notify(self.state.current_image, "set_image")

  def edge_detection(self):
        line_popup = EdgeDetectionPopup(self.parent)
        self.parent.wait_window(line_popup.top)
        selected_value = line_popup.selected_value

        kernel = None
        if selected_value == "+45":
            kernel = np.array([
                [-2,-1,0],
                [-1,0,1],
                [0,1,2]
            ])
        elif selected_value == "-45":
            kernel = np.array([
                [0,1,2],
                [-1,0,1],
                [-2,-1,0]
            ])
        elif selected_value == "Vertical":
            kernel = np.array([
                [-1,0,1],
                [-2,0,2],
                [-1,0,1]
            ])
        else:
            kernel = np.array([
                [-1,-2,-1],
                [0,0,0],
                [1,2,1]
            ])
        enhanced = self.opencv_helper.apply_filter(self.state.current_image, kernel)
        self.update_state(f"{selected_value} edge detection", enhanced)
        self.image_app_mediator.notify(self.state.current_image, "set_image")


  def thresholding(self):
      threshold_popup = ThresholdingPopup(self.parent)
      self.parent.wait_window(threshold_popup.top)
      selected_value = threshold_popup.selected_value
      if selected_value is not None:
          print(f"Thresholding Value Selected: {selected_value}")
          

  def custom_detection(self):
          
      custom_popup = CustomPopup(self.parent)
      self.parent.wait_window(custom_popup.top)
      kernel = custom_popup.entered_values
      print(kernel)
