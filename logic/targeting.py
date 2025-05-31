# given a list of detections, select the target based on preferred classes or highest confidence. 
# the function returns the center coordinates of the target in the specified region.
import torch
import math
import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

def get_mouse_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

# detections: [N, 6] -> x, y, w, h, conf, cls
# Prioritize the nearest target
def select_target(
    detections: torch.Tensor,
    preferred_cls = [1, 3, 0, 2],  # [ct_head, t_head, ct, t]
    region=[0, 0, 1920, 1080],
    minconf=0.5,
    mouse_xy=(960, 540)
) -> tuple[int, int] | None:
    if type(region) == dict:
        region = [region["left"], region["top"], region["width"], region["height"]]

    if detections is None or len(detections) == 0:
        return None

    region_x, region_y, region_w, region_h = region

    def distance(p1, p2):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    def find_closest():
        closest = None
        min_dist = float('inf')
        for det in detections:
            x, y, w, h, conf, cls = det
            if conf < minconf:
                continue
            cx = int(x.item() * region_w + region_x)
            cy = int(y.item() * region_h + region_y)
            if cls == 0 or cls == 2:  # ct or t
                cy -= int((h.item() * region_h) / 3)  # 向上偏移 1/3 检测框高
            dist = distance((cx, cy), mouse_xy)
            if dist < min_dist:
                min_dist = dist
                closest = (cx, cy)
        return closest

    target = find_closest()
    return target



# Prioritize the nearest head target, then body target
def select_target2(
    detections: torch.Tensor,
    preferred_cls = [1, 3, 0, 2],  # [ct_head, t_head, ct, t]
    region=[0, 0, 1920, 1080],
    minconf=0.5,
    mouse_xy=(960, 540)
) -> tuple[int, int] | None:
    if detections is None or len(detections) == 0:
        return None

    head_classes = preferred_cls[:2]
    body_classes = preferred_cls[2:]

    region_x, region_y, region_w, region_h = region

    def distance(p1, p2):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    def find_closest(classes, is_body=False):
        closest = None
        min_dist = float('inf')
        for det in detections:
            x, y, w, h, conf, cls = det
            if conf < minconf:
                continue
            if int(cls.item()) in classes:
                cx = x.item() * region_w + region_x
                cy = y.item() * region_h + region_y
                if is_body:
                    cy -= (h.item() * region_h) / 3  # 向上偏移 1/3 检测框高
                dist = distance((cx, cy), mouse_xy)
                if dist < min_dist:
                    min_dist = dist
                    closest = (int(cx), int(cy))
        return closest

    # 先找 head
    target = find_closest(head_classes)
    if target:
        return target

    # 再找 body，并且对 cy 向上偏移 1/3
    return find_closest(body_classes, is_body=True)

# detection = torch.tensor([[0.4933, 0.5409, 0.0677, 0.3022, 0.9205, 0.0000],
#         [0.4921, 0.4201, 0.0239, 0.0527, 0.7517, 1.0000]])
# select_target(detection, preferred_cls=[1,3,0,2], region=[0, 0, 1920, 1080])