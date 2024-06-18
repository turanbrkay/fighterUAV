from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO("yolov8s.yaml")

# training for small objects
# model = YOLO('yolov8s-p2.yaml').load('yolov8s.pt')

results = model.train(data="custom.yaml", epochs=100, device='gpu',imgsz=640)
