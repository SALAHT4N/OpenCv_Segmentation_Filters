import tkinter as tk
from tkinter import ttk

class AppStyles:
    @staticmethod
    def get_dark_mode_style():
        return {
            'background': '#2c2c2c',
            'top-frame': '#2c2c2c',
            'foreground': 'white',
            'bottom-frame': '#1e1e1e',
            'menu': '#2c2c2c'
        }
    
    def apply_styles(root, styles):
      root.tk_setPalette(styles['background'])

      style = ttk.Style()
      style.configure('Dark.Horizontal.TScale', background=styles['background'], foreground=styles['foreground'])
      style.map('Dark.Horizontal.TScale', background=[('selected', styles['background'])])

      style.configure('Dark.TRadiobutton', background=styles['background'], foreground=styles['foreground'])
      style.map('Dark.TRadiobutton', background=[('selected', styles['background'])])

      style.configure('Dark.TLabel', background=styles['background'], foreground='white')
      style.configure('Dark.TMenubutton', background=styles['menu'], foreground='white')
      style.configure('Dark.TMenu', background=styles['menu'], foreground='white')
      style.configure('Dark.TMenu.Tearoff', background=styles['menu'], foreground='white')
      style.configure('Dark.TMenuItem', background=styles['menu'], foreground='white')