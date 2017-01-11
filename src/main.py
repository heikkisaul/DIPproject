__author__ = 'Taavi'

from calculator import CoordsCalculator
import cv2
from tracker_example import *
from visualizer import *
from time import sleep


def result(coords):
    print(str(coords[0])+" "+str(coords[1]))

if __name__ == '__main__':

    calculator = CoordsCalculator(100, 2)
    visualizer = Visualizer(calculator)

    tracker = Tracker((30,90,90), (40,160,160))
    tracker.on_frame_processed = calculator.calculate_coords

    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        visualizer.update_frame(frame)
        tracker.process_frame(frame)