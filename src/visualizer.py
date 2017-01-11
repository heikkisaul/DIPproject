__author__ = 'Taavi'
import cv2


class Visualizer:

    def __init__(self, calculator):

        self.frame = None
        self.coord_array = []
        calculator.on_coords_calculated = self.display

    def update_frame(self, frame):
        self.frame = frame

    def display(self, coords):
        x = int(coords[0])
        y = int(coords[1])

        self.coord_array.append((x, y))

        cv2.circle(self.frame, (x, y), 30, (255, 0, 0), 1)

        for coord in self.coord_array:
            cv2.circle(self.frame, (x, y), 5, (0, 0, 255), -1)

        cv2.imshow('Name', self.frame)


