# model training
# For details, see：
# https://docs.ultralytics.com/modes/train/

import os
def train_yolo():
    os.system("yolo detect train data=cs_train_pics/data.yaml model=yolo11s.pt imgsz=640 epochs=200 device=0")


# CLI command
#yolo detect train data=cs_train_pics/data.yaml model=yolo11s.pt imgsz=640 epochs=200 device=0


# python code
from ultralytics import YOLO

# model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("yolo11s.pt")  # load a pretrained model (recommended for training)
# model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

results = model.train(data="yolo11-cs2/data.yaml", epochs=100, imgsz=64, device=0)