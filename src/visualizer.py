__author__ = 'Taavi'
import cv2

class Visualizer:

    def __int__(self):
        self.frame = None
        self.coord_array = []

    def update_frame(self, frame):
        self.frame = frame

    def display(self, coords):
        self.coord_array.append(coords)

        cv2.circle(self.frame, coords, 30, (255, 0, 0), 1)

        for coord in self.coord_array:
            cv2.circle(self.frame, coord, 5, (0, 0, 255), -1)

        cv2.imshow(self.frame)


