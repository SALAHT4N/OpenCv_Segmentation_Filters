import tkinter as tk
from tkinter import filedialog

class FileMenuBar:
  def __init__(self, parent, image_app_mediator, state, opencv_helper):
      self.menu_bar = tk.Menu(parent)
      self.image_app_mediator = image_app_mediator
      self.state = state
      self.opencv_helper = opencv_helper

      self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
      self.file_menu.add_cascade(label="Open", menu=self.create_open_submenu())
      self.file_menu.add_command(label="Save", command=self.save_file)
      self.menu_bar.add_cascade(label="File", menu=self.file_menu)

  def create_open_submenu(self):
      open_submenu = tk.Menu(self.file_menu, tearoff=0)
      open_submenu.add_command(label="Open as Grayscale", command=self.open_as_grayscale)
      open_submenu.add_command(label="Open as RGB", command=self.open_as_rgb)
      return open_submenu
    
  def open_as_grayscale(self):
      filepath = self.open_file()
      if filepath:
          self.state.current_image_path = filepath
          cv_image = self.opencv_helper.open_as_grayscale(filepath)
          self.update_current_image_state(cv_image)

  def open_as_rgb(self):
      filepath = self.open_file()
      if filepath:
        cv_image = self.opencv_helper.open_as_rgb(filepath)
        self.update_current_image_state(cv_image)

  def open_file(self):
      filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
      self.state.current_image_path = filepath
      return filepath
  
  def update_current_image_state(self, cv_image):
      self.state.applied_filters.clear()
      self.state.images_history.clear()

      self.state.set_current_image(cv_image)
      self.state.add_image(cv_image)
      self.state.add_filter("Initial")
      self.image_app_mediator.notify(cv_image, "set_image")

  def save_file(self):
      save_directory = filedialog.askdirectory()

      if save_directory:
          output_image_path = f"{save_directory}/{self.state.current_image_path.split('/')[-1]}_enhanced_image.jpg"

          self.opencv_helper.save_image(output_image_path, self.state.images_history[-1])
          print(f"Image saved to: {output_image_path}")

