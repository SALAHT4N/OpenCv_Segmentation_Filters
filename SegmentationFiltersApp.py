import tkinter as tk
from components.file_menu_bar import FileMenuBar
from components.filter_buttons_view import FilterButtonsView
from components.applied_filters_view import AppliedFiltersView
from components.image_view import ImageView
from shared.application_state import ApplicationState

class ImageApp:
    def __init__(self, root, title, state):
        self.root = root
        self.root.title(title)

        self.menubar = FileMenuBar(root, state)
        self.filter_buttons_view = FilterButtonsView(root, state)
        self.applied_filters_view = AppliedFiltersView(root, state)
        self.image_view = ImageView(root, state)
        self.root.config(menu = self.menubar.menu_bar)


if __name__ == "__main__":
    state = ApplicationState()
    root = tk.Tk()
    
    app = ImageApp(
        root=root, 
        title="Segmentation Filters",
        state=state)
    
    root.geometry("1000x460")
    root.mainloop()
