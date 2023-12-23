import tkinter as tk

class ImageView:
  def __init__(self, parent, image_app_mediator):
      self.image_app_mediator = image_app_mediator
      self.view = tk.Frame(parent)
      self.view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      self.image_label = tk.Label(self.view)
      self.image_label.pack(fill=tk.BOTH, expand=True)

  def display_image(self, photo):
      self.image_label.config(image=photo)
      self.image_label.image = photo