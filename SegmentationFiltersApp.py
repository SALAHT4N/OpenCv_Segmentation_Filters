import tkinter as tk
import cv2 as cv
from components.file_menu_bar import FileMenuBar
from components.filter_buttons_view import FilterButtonsView
from components.applied_filters_view import AppliedFiltersView
from components.image_view import ImageView
from shared.application_state import ApplicationState
from PIL import Image, ImageTk
import numpy as np

class OpenCvHelper: # facade pattern to simplify OpenCv (better testability, low coupling)
    def open_as_grayscale(self, path):
        return cv.imread(path, cv.IMREAD_GRAYSCALE)

    def open_as_rgb(self, path):
        return cv.imread(path, cv.IMREAD_UNCHANGED)
    
    def save_image(self, path,image):
        cv.imwrite(path, image)
    
    def apply_filter(self, image, kernel):
        return cv.filter2D(image, -1, kernel)
    
    def remove_response_lower_than_threshold(self, image, image_enhanced, threshold):
        for i in range(image_enhanced.shape[0]):
            for j in range (image_enhanced.shape[1]):
                print(f"image enhanced: {image_enhanced[i, j]}")
                print(f"image: {image[i, j]}")
                image_enhanced[i, j] = 0 if abs(int(image_enhanced[i, j] - image[i, j])) < threshold else image_enhanced[i, j]
        

class ImageConverter:
    def convert_cv_to_tinkter(self, cv_image):
        cv_image_rgb = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image_rgb)
        pil_image.thumbnail((700, 400))
        return ImageTk.PhotoImage(pil_image)

class ImageAppMediator:
    def __init__(self, root, title, state, opencv_helper, image_converter):
        self.root = root
        self.state = state
        self.root.title(title)
        self.opencv_helper = opencv_helper
        self.image_converter = image_converter

        self.menubar = FileMenuBar(root, self, state, opencv_helper)
        self.filter_buttons_view = FilterButtonsView(root, self, state, opencv_helper)
        self.applied_filters_view = AppliedFiltersView(root, self)
        self.image_view = ImageView(root, self)
        self.root.config(menu = self.menubar.menu_bar)
    
    def notify(self, data, command):
        tokens = command.split(" ")

        if tokens[0] == "set_image":          
            image = self.image_converter.convert_cv_to_tinkter(data)
            self.image_view.display_image(image)
            


if __name__ == "__main__":
    state = ApplicationState()
    root = tk.Tk()

    app = ImageAppMediator(
        root=root, 
        title="Segmentation Filters",
        state=state,
        opencv_helper=OpenCvHelper(),
        image_converter=ImageConverter())
    
    root.geometry("1000x460")
    root.mainloop()
