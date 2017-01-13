__author__ = 'Taavi'

from calculator import CoordsCalculator
import cv2
from tracker import *
import time

if __name__ == '__main__':
	
	# Display history size
    COORD_ARRAY_LENGTH = 50

    calculator = CoordsCalculator(150)
    tracker = Tracker((30,90,90), (40,220,220))
	
	# Find a camera and start vide capturing
    capture = cv2.VideoCapture(0)
	
    start_time = int(round(time.time() * 1000))

    coord_array = []

    while(True):
		# Read frame and save timestamp
        ret, frame = capture.read()
        timestamp = int(round(time.time() * 1000)) - start_time

        coords = calculator.calculate_coords(tracker.process_frame(frame), timestamp)
		
		# At the beginning when there is not enough data the calculator returns a couple of None's
        if coords is not None:
            x = int(coords[0])
            y = int(coords[1])

            if len(coord_array) >= COORD_ARRAY_LENGTH:
                coord_array.pop(0)

            coord_array.append((x, y))
			
			# Draw trajectory
            for coord in coord_array:
                cv2.circle(frame, coord, 5, (0, 0, 255), -1)
		
		# Display image with drawn trajectory
        cv2.imshow('elevant', frame)
		
		# Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
	
	# Finalize capturing
    capture.release()
    cv2.destroyAllWindows()

