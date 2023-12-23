import tkinter as tk
from tkinter import filedialog

class FileMenuBar:
  def __init__(self, parent, state):
      self.state = state
      self.menu_bar = tk.Menu(parent)

        # File menu
      self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
      self.file_menu.add_cascade(label="Open", menu=self.create_open_submenu())
      self.file_menu.add_command(label="Save", command=self.save_file)
      self.menu_bar.add_cascade(label="File", menu=self.file_menu)

  def create_open_submenu(self):
      open_submenu = tk.Menu(self.file_menu, tearoff=0)
      open_submenu.add_command(label="Open as Grayscale", command=self.open_as_grayscale)
      open_submenu.add_command(label="Open as RGB", command=self.open_as_rgb)
      return open_submenu
    
  def open_file(self):
      file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
      if file_path:
          self.display_image(file_path)

  def open_as_grayscale(self):
      # Add your code to open image as grayscale here
      self.open_file()
      pass

  def open_as_rgb(self):
      # Add your code to open image as RGB here
      self.open_file()
      pass

  def save_file(self):
        # Add your code to save the current image here
      pass
