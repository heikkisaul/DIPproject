__author__ = 'Taavi'


import numpy as np

f = open("data3.txt")
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

