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

    while True:
        ret, frame = capture.read()
        print(calculator.calculate_coords(tracker.process_frame(frame)))
