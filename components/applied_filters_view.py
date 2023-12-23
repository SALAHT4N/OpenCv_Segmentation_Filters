import tkinter as tk

class AppliedFiltersView:
  def __init__(self, parent, state):
      self.state = state
      self.parent = parent
      self.view = tk.Frame(self.parent)
      self.view.pack(side=tk.RIGHT, fill=tk.Y)
      self.scrollbar = tk.Scrollbar(self.view, orient=tk.VERTICAL)
      self.listbox = tk.Listbox(self.view, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
      self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      self.scrollbar.config(command=self.listbox.yview)
      self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

      self.listbox.bind("<<ListboxSelect>>", self.on_selection)

  def on_selection(self, event):
      selected_index = self.listbox.curselection()
      if selected_index:
          print(f"Selected Element: {self.listbox.get(selected_index)}")