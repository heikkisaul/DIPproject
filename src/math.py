__author__ = 'Taavi'


import numpy as np
import time


class Calculator:

    def __init__(self, size, rank):
        self.size = size
        self.rank = rank
        self.history_full = False
        self.current_index = 0

        self.start_time = int(round(time.time() * 1000))

        self.x_coefs = []
        self.y_coefs = []

        self.x_buf = []
        self.y_buf = []
        self.time_buf = []

        self.on_coords_calculated = None

    def calculate_coord(self, coords):
        if coords is not None:
            current_time = int(round(time.time() * 1000)) - self.start_time

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

            self.x_coefs = np.polyfit(self.time_buf, self.x_buf, self.rank)
            self.y_coefs = np.polyfit(self.time_buf, self.y_buf, self.rank)

            self.on_coords_calculated(coords[0], coords[1])

        else:
            current_time = int(round(time.time() * 1000)) - self.start_time


    def predict(self, current_time):

        for coef in self.x_coefs:


f = open("../data/data3.txt")
lines = f.read().split('\n')

x = []
y = []

for line in lines:
    parts = line.split('\t')

    if len(parts) < 2:
        continue

    x.append(float(parts[0]))
    y.append(float(parts[1]))

for n in range(len(x)):
    print("x="+str(x[n])+" y="+str(y[n]))

a = np.polyfit(x, y, 2)

print(a)

