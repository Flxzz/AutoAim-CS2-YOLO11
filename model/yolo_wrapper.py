from ultralytics import YOLO
import torch

class YOLOModel:
    def __init__(self, model_path="best.pt"):
        self.model = YOLO(model_path)

    def predict(self, image_tensor, conf = 0.25):
        return self.model(image_tensor, conf = conf)

    def infer(self, image_tensor, conf = 0.25):
        results = self.model(image_tensor, conf = conf)
        boxes = results[0].boxes
        xywhn = boxes.xywhn
        conf = boxes.conf.unsqueeze(1)
        clss = boxes.cls.unsqueeze(1)
        xywhn_conf_clss = torch.cat([xywhn, conf, clss], dim=1)
        xywhn_conf_clss = xywhn_conf_clss.cpu()
        return xywhn_conf_clss  # Tensor with [x1, y1, x2, y2, conf, cls]
