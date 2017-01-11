__author__ = 'Taavi'

import cv2


class Tracker:

    def __init__(self, HSV_lowerbound, HSV_upperbound):
        #Register callback to this variable
        self.on_frame_processed = None
        self.lowerbound = HSV_lowerbound
        self.upperbound = HSV_upperbound

    def process_frame(self, frame):

        # convert to HSV
        hsv_f = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # blur to reduce noise
        hsv_f = cv2.GaussianBlur(hsv_f, (11, 11), 0)
        # create thresholded mask image
        mask = cv2.inRange(hsv_f, self.lowerbound, self.upperbound)

        # Find contours on mask image
        contour = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # If there are any contours, calculate center coordinate for biggest one
        if len(contour) > 0:
            c = max(contour, key=cv2.contourArea)
            M = cv2.moments(c)
            if int(M["m00"]) == 0:
                center = None
            else:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        return center