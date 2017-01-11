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

    while(True):
        ret, frame = capture.read()

        coords = calculator.calculate_coords(tracker.process_frame(frame))

        if coords is not None:
            x = int(coords[0])
            y = int(coords[1])

            coord_array.append((x, y))

            for coord in coord_array:
                cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

        cv2.imshow('elevant', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

