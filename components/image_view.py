import tkinter as tk
from PIL import Image, ImageTk

class ImageView:
  def __init__(self, parent, state):
      self.state = state
      self.view = tk.Frame(parent)
      self.view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      self.image_label = tk.Label(self.view)
      self.image_label.pack(fill=tk.BOTH, expand=True)

  def display_image(self, file_path):
      image = Image.open(file_path)
      image.thumbnail((700, 400))  
      photo = ImageTk.PhotoImage(image)
      self.image_label.config(image=photo)
      self.image_label.image = photo