__author__ = 'Taavi'


import numpy as np
import time


class CoordsCalculator:

    def __init__(self, size, rank):
        self.size = size
        self.rank = rank
        self.history_full = False
        self.last_visible = True
        self.current_index = 0

        self.x_coefs = []
        self.y_coefs = []

        self.x_buf = []
        self.y_buf = []
        self.time_buf = []

        self.on_coords_calculated = None

    def calculate_coords(self, coords, timestamp):
        if coords is not None:
            self.last_visible = True

            if len(self.time_buf) >= self.size:
                self.x_buf.pop(0)
                self.y_buf.pop(0)
                self.time_buf.pop(0)

            self.x_buf.append(coords[0])
            self.y_buf.append(coords[1])
            self.time_buf.append(timestamp)

            return coords[0], coords[1]

        else:
            if self.last_visible:
                if len(self.time_buf) < 5:
                    return None

                self.last_visible = False

                print("Objest lost, calculating coefs based of num of coords:")
                print(len(self.time_buf))

                self.x_coefs = np.polyfit(self.time_buf, self.x_buf, 3)
                self.y_coefs = np.polyfit(self.time_buf, self.y_buf, 3)

                print("Calculated coefs:")
                print(self.x_coefs)

                self.history_full = False

                self.x_buf = []
                self.y_buf = []
                self.time_buf = []

            px, py = self.guess(timestamp)

            return px, py

    def guess(self, t):
        ret_x = (self.x_coefs[0] * t * t * t) + (self.x_coefs[1] * t * t) + (self.x_coefs[2] * t) + self.x_coefs[3]
        ret_y = (self.y_coefs[0] * t * t * t) + (self.y_coefs[1] * t * t) + (self.y_coefs[2] * t) + self.y_coefs[3]

        return ret_x, ret_y
