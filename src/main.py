__author__ = 'Taavi'

from calculator import CoordsCalculator
import cv2
from tracker_example import *
from visualizer import *
from time import sleep

def result(in_coords):
    print(in_coords)

if __name__ == '__main__':

    calculator = CoordsCalculator(100, 2)
    calculator.on_coords_calculated = result

    tracker = Tracker((30, 90, 90), (40, 160, 160))
    tracker.on_frame_processed = calculator.calculate_coords

    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        tracker.process_frame(frame)
