import torch
import numpy as np
import cv2
from time import time
import datetime
from ultralytics import YOLO
import os

#qr = cv2.QRCodeDetector()


class UAVDetector:
    def __init__(self, video_path, model_path):
        """
        hangi kamerayı kullancağımız, hangi modeli kullanacağımız ekran kartı mı yoksa işlemci mi kullanacağız
        ve bazı değişkenlere atama yapıyoruz
        """
        self.video_path = video_path
        self.model = self.load_model(model_path)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

    def get_video_capture(self):
        """
        kameradan görüntü alıyoruz
        """
        return cv2.VideoCapture(self.video_path)

    def load_model(self,model_path):
        return YOLO(model_path)

    def model_results(self, frame):
        """
        modelden alınan sonuçları döndürür
        """
        results = self.model(frame)[0]

        labels = results.names  # Tüm sınıf adlarını alın
        boxes = results.boxes.xyxy  # Tüm sınırlayıcı kutuların koordinatlarını alın
        scores = results.boxes.conf  # Tüm güven skorlarını alın
        class_ids = results.boxes.cls  # Tüm sınıf kimliklerini alın

        return labels, boxes, scores, class_ids

    def class_to_label(self, x):
        """
        classlarımızı labela dönüştürüyoruz.
        """
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        """
        Algılanan nesnelerin sınırlayıcı kutularını çizer ve etiketlerini yazar.
        """
        labels, boxes, scores, class_ids = results
        frame_height, frame_width = frame.shape[:2]
        scale_factor = min(frame_width, frame_height) / 1000.0

        for i in range(len(scores)):
            if scores[i] > 0.7:
                box = boxes[i]
                x1, y1, x2, y2 = box
                label = labels[int(class_ids[i])]

                frame_center_x = (x1 + x2) // 2
                frame_center_y = (y1 + y2) // 2

                color = (0, 255, 0)  # Varsayılan renk yeşil
                if self.isObjectFit(box, frame_width, frame_height):
                    color = (0, 0, 255)  # Kırmızı

                cv2.line(frame, (frame_width // 2, frame_height // 2), (int(frame_center_x), int(frame_center_y)),
                         color, 2)
                cv2.circle(frame, (int(frame_width // 2), int(frame_height // 2)), radius=3, color=color,
                           thickness=-1)
                cv2.circle(frame, (int(frame_center_x), int(frame_center_y)), radius=3, color=color, thickness=-1)

                # target center coordinate
                text = f'Target: ({frame_center_x}, {frame_center_y})'
                cv2.putText(frame, text, (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            color, 1)

                # detected target
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        return frame
    def drawLockdownRectangle(self,frame):
        #! Kilitlenme dörgenini çiz.
        height, width = frame.shape[:2]

        # Sol, sağ, üst ve alt kenarlardan bırakılacak uzunlukları hesapla
        left_padding = int(0.25 * width)
        right_padding = int(0.25 * width)
        top_padding = int(0.1 * height)
        bottom_padding = int(0.1 * height)

        # Dikdörtgenin köşe koordinatlarını hesapla
        x1 = left_padding
        y1 = top_padding
        x2 = width - right_padding
        y2 = height - bottom_padding

        # Dikdörtgeni çiz.
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        return frame
    def drawFPStext(self, frame, fps):
        text_size, _ = cv2.getTextSize(f'FPS: {int(fps)}', cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        text_width, text_height = text_size

        # FPS yazısını frame boyutuna oranlayarak sol üst köşede tutma
        text_x = 10  # Sol kenardan 10 piksel içeride
        text_y = text_height + 10  # Üst kenardan 10 piksel içeride

        # FPS yazısını çizme
        cv2.putText(frame, f'FPS: {int(fps)}', (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        return frame
    def drawTimeText(self, frame, time):
        height, width = frame.shape[:2]
        text = str(time)
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        font_scale = 0.7
        font_thickness = 2

        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_width, text_height = text_size

        cv2.putText(frame, text, (int(width - text_width - 5), 20), cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                    (255, 255, 255), font_thickness)

        return frame

    def isObjectFit(self, box, frame_width, frame_height):
        """
        Eğer tespit edilen objenin yatay veya dikey uzunluğu frame'in yüzde 5'ine eşit veya büyükse True döner.
        """
        x1, y1, x2, y2 = box
        box_width = x2 - x1
        box_height = y2 - y1

        if box_width >= 0.05 * frame_width or box_height >= 0.05 * frame_height:
            return True
        return False

    def save_video(frames):
        fps = 30
        video_path = 'save_test.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'h264')
        video_writer = cv2.VideoWriter(video_path, fourcc, fps, (600, 480))

        for frame in frames:
            video_writer.write(frame)

        video_writer.release()
    def __call__(self):
        """
        kameramızı açarak aranan nesnenin nerede olduğunu hangi nesne olduğunu ve % kaç olasılıkla onun olduğunu yazıyoruz.
        """

        cap = self.get_video_capture()

        out = cv2.VideoWriter("./output_video.mp4", cv2.VideoWriter_fourcc(*'X264'), int(cap.get(cv2.CAP_PROP_FPS)),
                              (600, 800))

        #cap = self.get_video_capture()
        assert cap.isOpened()

        while True:
            ret, frame = cap.read()
            assert ret

            #frame = cv2.resize(frame, (416, 416))

            height, width = frame.shape[:2]

            start_time = time()
            results = self.model_results(frame)
            frame = self.plot_boxes(results, frame)
            end_time = time()

            fps = 1 / np.round(end_time - start_time, 2)
            t = datetime.datetime.now()
            x = (t.strftime("%X,%f"))


            print(x)

            self.drawLockdownRectangle(frame)
            self.drawFPStext(frame, fps)
            self.drawTimeText(frame, x)

            cv2.imshow('YOLOv8 Detection', frame)

            self.save_video(frame)
            out.write(frame)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()



detector = UAVDetector(video_path="./videos/video2.mp4", model_path='./runs/detect/train/weights/last.pt')
detector()
