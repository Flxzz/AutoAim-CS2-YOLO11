# turn np.array to torch.tensor
import torch
import cv2
import numpy as np

# image type: torch.tensor -> BCHW(1,3,H,W)
def preprocess(image: np.ndarray, img_size: int = 640) -> torch.Tensor:
    image_resized = cv2.resize(image, (img_size, img_size))
    # image_rgb = image_resized[..., ::-1]
    image_rgb = image_resized
    image_tensor = torch.from_numpy(image_rgb.copy()).permute(2, 0, 1).float() / 255.0
    return image_tensor.unsqueeze(0)  # (1, 3, H, W)
