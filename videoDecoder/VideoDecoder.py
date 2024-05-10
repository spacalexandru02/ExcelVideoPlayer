import cv2
import xlwings as xw
import numpy as np

class VideoDecoder:
    def __init__(self):
        self.wb = xw.Book('player2.xlsx')
        self.sht1 = self.wb.sheets['Sheet1']

    def frame_to_hex_matrix(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = rgb_frame.shape
        hex_matrix = np.empty((height, width), dtype=object)
        for i in range(height):
            for j in range(width):
                r, g, b = rgb_frame[i, j]
                hex_color = '#{0:02x}{1:02x}{2:02x}'.format(b, g, r)
                hex_matrix[i, j] = hex_color

        return hex_matrix


    def analyze(self, video_path):
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                print("Error: Unable to open video file.")
                return

            try:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    hexa = self.frame_to_hex_matrix(frame)
                    self.sht1['A1'].value = hexa
                    cv2.imshow('Frame', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()

            except Exception as e:
                print("Error:", str(e))
                cap.release()
                cv2.destroyAllWindows()



