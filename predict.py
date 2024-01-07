from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator
# Load a model
model = YOLO("yolov8n.yaml")
model = YOLO("runs/detect/train13/weights/best.pt")
img = "predictors/p2.jpg"#"football-players-detection-4/train/images/2e57b9_1_8_png.rf.3ad6daa99d04cabafdb0a2d7a80d68dc.jpg"
results = model(img,save = True)
# for r in results:
#     print(r.boxes)     