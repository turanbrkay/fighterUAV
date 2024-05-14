from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO("yolov8s.yaml")

results = model.train(data="data.yaml", epochs=100, device='gpu')
