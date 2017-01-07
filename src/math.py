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

        self.history = []

    def calculate_coord(self, coords):
        if coords is not None:
            current_time = int(round(time.time() * 1000))

            if not self.history_full:
                self.history.append((current_time, coords[0], coords[1]))
                self.current_index += 1

                if self.current_index == self.size:
                    self.history_full = True
            else:
                self.history.pop(0)
                self.history.append((current_time, coords[0], coords[1]))




    def predict(self):


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

