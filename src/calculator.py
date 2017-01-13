__author__ = 'Taavi Adamson, Heikki Saul'

"""
calculator.py
Contains CoordsCalculator class that handles location approximation
"""


import numpy as np
import time


class CoordsCalculator:
	
    # Initialization with given history size
    def __init__(self, size):
        self.size = size
        self.last_visible = True
        self.current_index = 0

        self.x_coefs = []
        self.y_coefs = []

        self.x_buf = []
        self.y_buf = []
        self.time_buf = []

        self.on_coords_calculated = None

    # Main method used, takes in a tuple of coordinates (x, y) and frame timestamp
    # Returns the same coordinate if the coordinate is known
    #		  predicts coordinate if given coordinate is None

    def calculate_coords(self, coords, timestamp):
        # Two main cases:

        # Means the object is visible
        if coords is not None:

            self.last_visible = True

            # Save coordinates to history, keep size restrictions
            if len(self.time_buf) >= self.size:
                self.x_buf.pop(0)
                self.y_buf.pop(0)
                self.time_buf.pop(0)

            self.x_buf.append(coords[0])
            self.y_buf.append(coords[1])
            self.time_buf.append(timestamp)

            # Return given coordinates
            return coords[0], coords[1]

        # Object not visible
        else:

            # To make sure the curve is calculated only once
            if self.last_visible:
                if len(self.time_buf) < 5:
                    print("Not enough data")
                    return None

                self.last_visible = False

                # Calculate best fitting curves for the saved history of points
                self.x_coefs = np.polyfit(self.time_buf, self.x_buf, 3)
                self.y_coefs = np.polyfit(self.time_buf, self.y_buf, 3)

                print("Calculated coefs:")
                print(self.x_coefs)
                print(self.y_coefs)

                self.x_buf = []
                self.y_buf = []
                self.time_buf = []

            px, py = self.guess(timestamp)

            return px, py

    # Helper function to calculate coordinates from timestamp
    def guess(self, t):
        ret_x = (self.x_coefs[0] * t * t * t) + (self.x_coefs[1] * t * t) + (self.x_coefs[2] * t) + self.x_coefs[3]
        ret_y = (self.y_coefs[0] * t * t * t) + (self.y_coefs[1] * t * t) + (self.y_coefs[2] * t) + self.y_coefs[3]

        return ret_x, ret_y
