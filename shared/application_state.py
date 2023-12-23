class ApplicationState:
  def __init__(self):
    self.applied_filters = []
    self.images_history = []
    self.current_image = None
    self.current_image_path = None

  def set_current_image(self, image):
    self.current_image = image

  def add_image(self, image):
    self.images_history.append(image)

  def add_filter(self, filter_name):
    self.applied_filters.append(filter_name)