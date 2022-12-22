import os
import cv2
import matplotlib.pyplot as plt


class Image(object):
    def __init__(self, image):
        self.image = image
        
    @classmethod
    def from_array(cls, array):
        return cls(image=array)

    @classmethod
    def from_file(cls, filename):
        if not os.path.exists(filename):
            raise ValueError(f'The image file \"{filename}\" does not exist.')
        
        raw_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        rgb = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
        return cls(image=rgb)
    
    @property
    def shape(self) -> tuple:
        return self.image.shape
    
    def display(self):
        """
        Display the loaded image.
        """
        print("Displaying rendered image...")
        plt.axis("off")
        plt.imshow(self.image)
        