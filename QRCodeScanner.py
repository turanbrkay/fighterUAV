import cv2
import numpy as np
from pyzbar.pyzbar import decode


class QRCodeScanner:
    def __init__(self, image_path, window_name='OpenCV pyzbar'):
        self.image_path = image_path
        self.window_name = window_name
        self.TARGETTEXT = ""

    def start(self):
        frame = cv2.imread(self.image_path)
        frame_copy = frame.copy()

        try:
            for d in decode(frame):
                s = d.data.decode()

                self.TARGETTEXT = s

                frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                      (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)

            # QR kodlarının içindeki alanları beyaz yap
            mask = np.zeros_like(frame[:, :, 0])
            for d in decode(frame):
                x, y, w, h = d.rect
                mask[y:y + h, x:x + w] = 255
            frame_copy[mask != 255] = 0  # Maskenin dışındaki pikselleri siyah yap

            cv2.imshow("Original Image", frame)
            cv2.imshow("Processed Image", frame_copy)
            cv2.waitKey(0)  # Ekranda beklet
        except Exception as e:
            print("Bir hata oluştu:", e)
            cv2.destroyAllWindows()  # Pencereyi kapat

        if self.TARGETTEXT != "":
            print("Veri okundu.")
        else:
            print("Veri okunamadı.")

        cv2.destroyAllWindows()  # Pencereyi kapat


# QRCodeScanner sınıfını kullanarak QR kodlarını bir görüntü dosyasından oku
image_path = "image3.jpg"  # Kullanmak istediğiniz görüntünün yolunu buraya yazın
qr_scanner = QRCodeScanner(image_path)
qr_scanner.start()
