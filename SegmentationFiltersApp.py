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
    
    def threshold(self, image, value):
        _, dst = cv.threshold(image, value, 255, 0)
        return dst
    
    def scale_up(self, image):
        copy = image.copy()
        for i in range(image.shape[0]):
            for j in range (image.shape[1]):
                copy[i][j] += 127
        return copy
    
    def zero_crossing(self, image):
        enhanced = image.copy()

        for i in range(image.shape[0]):
            for j in range (image.shape[1]):
                if (j-1 > 0 and j+1 < image.shape[1] and 
                    image[i][j] == 255 and (image[i][j-1] == 0 or image[i][j+1] == 0)):
                    continue
                enhanced[i][j] = 0
        return enhanced
        # minLoG = cv.morphologyEx(image, cv.MORPH_ERODE, np.ones((3,3)))
        # maxLoG = cv.morphologyEx(image, cv.MORPH_DILATE, np.ones((3,3)))
        # zeroCross = np.logical_or(np.logical_and(minLoG < 0,  image > 0), np.logical_and(maxLoG > 0, image < 0))

        # return zeroCross

    def automatic_thresholding(self, image):
        histogram = cv.calcHist([image], [0], None, [256], [0, 256])
        total_pixels = np.sum(histogram)

        gray_levels = np.arange(256)
        avg = np.sum(gray_levels * histogram.flatten()) / total_pixels

        difference = 255

        while difference >= 4:
            l = 0
            r = 255

            sum_left = 0
            sum_right = 0

            while l < avg:
                sum_left += histogram[int(l)][0]
                l += 1

            while r > avg:
                sum_right += histogram[int(r)][0]
                r -= 1

            avg_left = np.sum(np.arange(0, int(avg + 1)) * histogram[:int(avg) + 1].flatten()) / sum_left if sum_left > 0 else 0
            avg_right = np.sum(np.arange(int(avg), 256) * histogram[int(avg):].flatten()) / sum_right if sum_right > 0 else 0
            new_avg = (avg_left + avg_right) / 2
            difference = abs(new_avg - avg)

            avg = new_avg
            
        enhanced = self.threshold(image, new_avg)
        return (enhanced, avg)

    def laplacian_of_guassian(self, image):
        blurred = cv.GaussianBlur(image, (3, 3), 0) 
        laplacian = np.uint8(np.absolute(cv.Laplacian(blurred, cv.CV_64F)))
        return laplacian
    
    def remove_response_lower_than_threshold(self, image, image_enhanced, threshold):
        for i in range(image_enhanced.shape[0]):
            for j in range (image_enhanced.shape[1]):
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
        self.applied_filters_view = AppliedFiltersView(root, self, state)
        self.image_view = ImageView(root, self)
        self.root.config(menu = self.menubar.menu_bar)
    
    def notify(self, data, command):
        tokens = command.split(" ")

        if tokens[0] == "set_image":          
            image = self.image_converter.convert_cv_to_tinkter(data)
            self.image_view.display_image(image)
            self.applied_filters_view.listbox.insert(tk.END, self.state.applied_filters[-1])

        elif tokens[0] == "update_image":
            image = self.image_converter.convert_cv_to_tinkter(data)
            self.image_view.display_image(image)

        elif tokens[0] == "clear":
            self.applied_filters_view.listbox.delete(0, tk.END)


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
