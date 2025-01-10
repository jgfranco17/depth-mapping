from time import perf_counter
from typing import Optional

import numpy as np
import torch

from depth_mapping.shared.constants import MidasConstants


class MonocularMapper(object):
    def __init__(self, level: Optional[int] = 2) -> None:
        self.model_types = {
            1: MidasConstants.MODEL_SMALL,
            2: MidasConstants.MODEL_MEDIUM,
            3: MidasConstants.MODEL_LARGE,
        }

        # Set model
        self.model = torch.hub.load(
            MidasConstants.HUB_MODEL_REPO, self.model_types[level]
        )
        device_type = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device_type)
        self.model.to(self.device)
        self.model.eval()

        # Prepare transforms
        midas_transforms = torch.hub.load(MidasConstants.HUB_MODEL_REPO, "transforms")
        self.transform = midas_transforms.dpt_transform
        large_transform_models = [
            MidasConstants.MODEL_MEDIUM,
            MidasConstants.MODEL_LARGE,
        ]
        if self.model_types[level] in large_transform_models:
            self.transform = midas_transforms.dpt_transform
        else:
            self.transform = midas_transforms.small_transform

        print(f"Ready for monocular depth estimation, running on {device_type.upper()}")

    def map(self, image: np.ndarray) -> np.ndarray:
        """
        Generate map of estimated relative depth.

        Args:
            image: Image to map
        """
        # Transform the image for model input
        self.input_batch = self.transform(image).to(self.device)

        # Run model on the input image
        start_time = perf_counter()
        with torch.no_grad():
            prediction = self.model(self.input_batch)
            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=image.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()
        end_time = perf_counter()
        print(f"Elapsed modeling time: {end_time-start_time:.3f}s")

        # Return in array format
        return prediction.cpu().numpy()
