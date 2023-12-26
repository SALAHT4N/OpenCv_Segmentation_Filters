import tkinter as tk
from tkinter import ttk

class AppliedFiltersView:
  def __init__(self, parent, image_app_mediator, state):
      self.state = state
      self.image_app_mediator = image_app_mediator
      self.parent = parent
      self.view = tk.Frame(self.parent)
      self.view.pack(side=tk.RIGHT, fill=tk.Y)

      label = ttk.Label(self.view, text="Applied Filters", font=("Helvetica", 10),  style='Dark.TLabel')
      label.pack(side=tk.TOP, pady=5)

      self.scrollbar = tk.Scrollbar(self.view, orient=tk.VERTICAL)
      self.listbox = tk.Listbox(self.view, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
      self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      self.scrollbar.config(command=self.listbox.yview)
      self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

      self.listbox.bind("<<ListboxSelect>>", self.on_selection)

  def on_selection(self, event):
      selected_index = self.listbox.curselection()[0]
      if selected_index is not None:
          print(selected_index)
          self.state.current_image = self.state.images_history[selected_index]
          self.image_app_mediator.notify(self.state.images_history[selected_index], "update_image")