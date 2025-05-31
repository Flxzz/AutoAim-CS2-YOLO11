import yaml
import torch
from capture.grabber import grab
from preprocess.transform import preprocess
from model.yolo_wrapper import YOLOModel
from logic.targeting import select_target, get_mouse_position
from control.mouse import move_mouse_to
from utils.logger import setup_logger
import time


def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    cfg = load_config()
    log = setup_logger(log_file=cfg["log_file"])
    model = YOLOModel(cfg["model_path"])

    while True:
        frame = grab(region=cfg["screen_region"], use_gpu=cfg["use_gpu_capture"])
        img_tensor = preprocess(frame)
        detections = model.infer(img_tensor, conf = cfg["confidence_threshold"])
        mouse_position = get_mouse_position()
        target = select_target(detections, cfg["preferred_cls"], cfg["screen_region"], cfg["confidence_threshold"], mouse_xy=mouse_position)
        if target:
            # log.info(f"Target: {target}")
            move_mouse_to(*target)
            time.sleep(0.05)
        # time.sleep(0.05)


if __name__ == "__main__":
    main()
