__author__ = 'Taavi'

from calculator import CoordsCalculator
from time import sleep


def result(coords):
    print(str(coords[0])+" "+str(coords[1]))

if __name__ == '__main__':

    calculator = CoordsCalculator(100, 2)
    calculator.on_coords_calculated = result
    
    # Calculator test
    f = open("../data/data4.txt")
    lines = f.read().split('\n')

    for line in lines:
        parts = line.split(' ')

        if parts[1] == "None":
            calculator.calculate_coords(None)
        else:
            calculator.calculate_coords((float(parts[1]), float(parts[1])))

        sleep(0.001)
