import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


class Image(object):
    def __init__(self, image):
        self.image = image

    @classmethod
    def from_array(cls, array):
        return cls(image=array)

    @classmethod
    def from_file(cls, filename):
        if not os.path.exists(filename):
            raise ValueError(f'The image file "{filename}" does not exist.')

        raw_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
        rgb = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
        return cls(image=rgb)

    @property
    def shape(self) -> tuple:
        return self.image.shape

    def colormap(self, image) -> np.ndarray:
        """
        Recolor the depth map from grayscale to colored.

        Args:
            image (np.ndarray): Grayscale image

        Returns:
            np.ndarray: Colored map image
        """
        normalized_image = image.astype(np.uint8)
        return cv2.applyColorMap(normalized_image, cv2.COLORMAP_HOT)

    def display(self, recolor: bool = False):
        """
        Display the loaded image.
        """
        print("Displaying rendered image...")
        colored = lambda img: cv2.applyColorMap(img, cv2.COLORMAP_HOT)
        image = colored(self.image) if recolor else self.image
        plt.axis("off")
        plt.imshow(image)
