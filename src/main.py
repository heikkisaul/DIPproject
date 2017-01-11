__author__ = 'Taavi'

from calculator import CoordsCalculator
import cv2
from tracker_example import *
from visualizer import *
from time import sleep

if __name__ == '__main__':

    calculator = CoordsCalculator(100, 2)
    tracker = Tracker((30, 90, 90), (40, 160, 160))

    capture = cv2.VideoCapture(0)
    coord_array = []

    while True:
        ret, frame = capture.read()
        x_f, y_f = calculator.calculate_coords(tracker.process_frame(frame))

        x = int(x_f)
        y = int(y_f)

        coord_array.append((x, y))

        cv2.circle(frame, (x, y), 30, (255, 0, 0), 1)

        for coord in coord_array:
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

        cv2.imshow('Name', frame)
