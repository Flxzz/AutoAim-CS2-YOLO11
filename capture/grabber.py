# capture the specified area of ​​the screen

import numpy as np
import mss
import dxcam

# in: region  #out: np.array
def grab(region=[0,0,1920,1080], use_gpu=False) -> np.ndarray:
    if use_gpu:
        cam = dxcam.create()
        frame = cam.get_latest_frame()
    else:
        with mss.mss() as sct:
            monitor = region or sct.monitors[1]
            frame = np.array(sct.grab(monitor))
    return frame[..., :3]  # Return RGB
