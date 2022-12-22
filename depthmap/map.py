import torch
from time import perf_counter


class MonocularMapper(object):
    def __init__(self, level:int=2):
        self.model_types = {
            1: "MiDaS_small",
            2: "DPT_Hybrid",
            3: "DPT_Large"
        }
        
        # Set model 
        self.model = torch.hub.load("intel-isl/MiDaS", self.model_types[level])
        device_type = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device_type)
        self.model.to(self.device)
        self.model.eval()
        
        # Prepare transforms
        midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.transform = midas_transforms.dpt_transform  
        if self.model_types[level] in ["DPT_Large", "DPT_Hybrid"]:
            self.transform = midas_transforms.dpt_transform
        else:
            self.transform = midas_transforms.small_transform
            
        print(f'Ready for monocular depth estimation, running on {device_type.upper()}')
        
    def map(self, image):
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
                size=self._image.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()
        end_time = perf_counter()
        print(f'Elapsed time: {end_time-start_time}s')

        # Return in array format
        return prediction.cpu().numpy()
        