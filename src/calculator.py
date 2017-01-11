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

        self.start_time = int(round(time.time() * 1000))

        self.x_coefs = []
        self.y_coefs = []

        self.x_buf = []
        self.y_buf = []
        self.time_buf = []

        self.on_coords_calculated = None

    def calculate_coords(self, coords):

        current_time = int(round(time.time() * 1000)) - self.start_time

        if coords is not None:
            self.last_visible = True

            if not self.history_full:
                self.x_buf.append(coords[0])
                self.y_buf.append(coords[1])
                self.time_buf.append(current_time)

                self.current_index += 1

                if self.current_index == self.size:
                    self.history_full = True
            else:
                self.x_buf.pop(0)
                self.y_buf.pop(0)
                self.time_buf.pop(0)

                self.x_buf.append(coords[0])
                self.y_buf.append(coords[1])
                self.time_buf.append(current_time)

            return coords[0], coords[1]

        else:
            if self.last_visible:
                if len(self.time_buf) < 10:
                    return None

                self.last_visible = False

                print("Objest lost, calculating coefs")

                self.x_coefs = np.polyfit(self.time_buf, self.x_buf, 2)
                self.y_coefs = np.polyfit(self.time_buf, self.y_buf, 2)

                print("Calculated coefs:")
                print(self.x_coefs)

                self.history_full = False

                self.x_buf = []
                self.y_buf = []
                self.time_buf = []

            px, py = self.guess(current_time)

            return px, py

    def guess(self, t):
        ret_x = (self.x_coefs[0] * t * t) + (self.x_coefs[1] * t) + self.x_coefs[2]
        ret_y = (self.y_coefs[0] * t * t) + (self.y_coefs[1] * t) + self.y_coefs[2]

        return ret_x, ret_y
