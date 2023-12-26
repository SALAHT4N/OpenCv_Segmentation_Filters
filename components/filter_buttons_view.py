import tkinter as tk
from tkinter import ttk
import numpy as np
from popups.line_detection_frame import LineDetectionPopup
from popups.edge_detection_frame import EdgeDetectionPopup
from popups.thresholding_frame import ThresholdingPopup
from popups.custom_frame import CustomPopup

class FilterButtonsView:
  def __init__(self, parent, image_app_mediator, state, opencv_helper, styles):
      self.image_app_mediator = image_app_mediator
      self.view = tk.Frame(parent, width=150, background=styles['top-frame'])
      self.view.pack(side=tk.LEFT, fill=tk.Y)
      self.parent = parent
      self.opencv_helper = opencv_helper
      self.state = state

      filters_label = ttk.Label(self.view, text="Filters", font=("Helvetica", 10),  style='Dark.TLabel')
      filters_label.pack(side=tk.TOP, pady=5)

      button_names = ["Point Detection", "Line Detection", "Edge Detection", "LoG (2dFilter)", "Log (openCv)" , "Thresholding", "Custom", "Auto Thresholding", "Zero Crossing", "Adaptive Threshold","Scale Up"]
      button_handlers = [self.point_detection, self.line_detection, self.edge_detection, self.log_detection, self.log_detection_2,
                           self.thresholding, self.custom_detection, self.auto_thresholding, self.zero_crossing,self.adaptive_threshold, self.scale_up]

      for name, handler in zip(button_names, button_handlers):
          button = tk.Button(self.view, text=name, command=handler, width=15)
          button.pack(side=tk.TOP, pady=5)

  def update_state(self, filter_name, enhanced):
      self.state.add_filter(filter_name)
      self.state.add_image(enhanced)
      self.state.set_current_image(enhanced)

  def adaptive_threshold(self):
      enhanced = self.opencv_helper.adaptive_threshold(self.state.current_image)
      self.update_state("adaptive thresholding", enhanced)
      self.image_app_mediator.notify(self.state.current_image, "set_image")

  def point_detection(self):
      point_kernel = np.array(
          [
              [-1, -1, -1],
              [-1,  8, -1],
              [-1, -1, -1]
          ]
        )
      enhanced = self.opencv_helper.apply_filter(self.state.current_image, point_kernel)
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
    #   scaled_up = self.opencv_helper.scale_up(enhanced)
      self.update_state("Laplacian of Gaussian", enhanced)
      self.image_app_mediator.notify(enhanced, "set_image")

  def log_detection_2(self):
      enhanced = self.opencv_helper.laplacian_of_guassian(self.state.current_image)
    #   enhanced = self.opencv_helper.scale_up(enhanced)
      self.update_state("Laplacian of Guassian", enhanced)
      self.image_app_mediator.notify(self.state.current_image, "set_image")

  def scale_up(self):
      enhanced = self.opencv_helper.scale_up(self.state.current_image)
      self.update_state("Scaled up", enhanced)
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
          elif selected_value == "Horizontal":
              kernel = np.array([
                  [-1,-1,-1],
                  [2,2,2],
                  [-1,-1,-1]
              ])
          else:
              return
          
          enhanced = self.opencv_helper.apply_filter(self.state.current_image, kernel)
          self.update_state(f"{selected_value} line detection", enhanced)
          self.image_app_mediator.notify(self.state.current_image, "set_image")

  def edge_detection(self):
        edge_popup = EdgeDetectionPopup(self.parent)
        self.parent.wait_window(edge_popup.top)
        selected_value = edge_popup.selected_value

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
        elif selected_value == "Horizontal":
            kernel = np.array([
                [-1,-2,-1],
                [0,0,0],
                [1,2,1]
            ])
        else:
            return
        enhanced = self.opencv_helper.apply_filter(self.state.current_image, kernel)
        self.update_state(f"{selected_value} edge detection", enhanced)
        self.image_app_mediator.notify(self.state.current_image, "set_image")


  def thresholding(self):
      threshold_popup = ThresholdingPopup(self.parent)
      self.parent.wait_window(threshold_popup.top)
      selected_value = threshold_popup.selected_value
      if selected_value is not None:
          enhanced = self.opencv_helper.threshold(self.state.current_image, selected_value)
          self.update_state(f"{selected_value} threshold", enhanced)
          self.image_app_mediator.notify(self.state.current_image, "set_image")

  def custom_detection(self):
      custom_popup = CustomPopup(self.parent)
      self.parent.wait_window(custom_popup.top)
      kernel = custom_popup.entered_values
      filter_name = custom_popup.name

      if kernel is not None:
          enhanced = self.opencv_helper.apply_filter(self.state.current_image, kernel)
          self.update_state(f"{filter_name} filter", enhanced)
          self.image_app_mediator.notify(self.state.current_image, "set_image")
      
  def auto_thresholding(self):
      enhanced, value = self.opencv_helper.automatic_thresholding(self.state.current_image)
      self.update_state(f"auto threshold {value}", enhanced)
      self.image_app_mediator.notify(self.state.current_image, "set_image")

  def zero_crossing(self):
    #   log_kernel = np.array(
    #       [
    #           [0,0,-1,0,0],
    #           [0,-1,-2,-1,0],
    #           [-1,-2,16,-2,-1],
    #           [0,-1,-2,-1,0],
    #           [0,0,-1,0,0],
    #       ]
    #   )
    #   enhanced = self.opencv_helper.apply_filter(self.state.current_image, log_kernel)
      enhanced = self.opencv_helper.laplacian_of_guassian(self.state.current_image)
      enhanced = self.opencv_helper.threshold(enhanced, 0)
      enhanced = self.opencv_helper.zero_crossing(enhanced)

      self.update_state(f"zero crossing", enhanced)
      self.image_app_mediator.notify(self.state.current_image, "set_image")