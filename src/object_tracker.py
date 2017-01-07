import cv2
import numpy as np
import time

# TODO hsv is very noisy, maybe use RGB and a calibration mechanism?
# TODO increase robustness of primary blob (currently gives "no blob" on a lot of frames)


def current_time_ms():
    return int(round(time.time() * 1000))


def threshold(frame,HSV_lower, HSV_upper):

    lowerbound = np.array(HSV_lower)
    upperbound = np.array(HSV_upper)

    frame = cv2.inRange(frame, lowerbound, upperbound)

    return frame


def blob_handling(frame):

    # apply filtering to increase detection robustness
    # TODO test possible filters for increased robustness
    kernel = np.ones((3,3),np.uint8)

    filtered_frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 200
    params.maxThreshold = 255

    # ignore small blobs
    params.filterByArea = True
    params.minArea = 10

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(filtered_frame)

    # if a blob fitting the parameters is detected, return frame and centre coordinates
    if len(keypoints) != 0:

        key_X = int(keypoints[0].pt[0])
        key_Y = int(keypoints[0].pt[1])

        key_coords = (key_X,key_Y)
        return filtered_frame, key_coords

    # if no fitting blob is detected, return frame and empty tuple
    else:
        return filtered_frame,()


if __name__ == '__main__':

    capture = cv2.VideoCapture(0)
    start_time = current_time_ms()

    while(True):
        ret, frame = capture.read()

        # converts to HSV for increased color robustness
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # applies threshold (currently for a small green jar lid, change values accordingly)
        # H = H/2 (0-180), S = 0-255, V = 0-255
        mask = threshold(hsv,[85, 20, 0],[100,255,255])

        blobim,centre_coord = blob_handling(mask)
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        hsv = cv2.bitwise_and(hsv,hsv,mask=blobim)

        # shows object in original frame (masked) and the filtered mask
        cv2.imshow('frame',hsv)
        cv2.imshow('blobs',blobim)

        print(centre_coord)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
