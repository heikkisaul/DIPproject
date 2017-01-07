__author__ = 'Taavi'


class Tracker:

    def __init__(self):
        #Register callback to this variable
        self.on_frame_processed = None

    def process_frame(self, frame):
        #Process frame
        coords = (0,0)
        self.on_frame_processed(coords)