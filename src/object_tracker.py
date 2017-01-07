import cv2
import numpy as np

def detect_contours(frame, HSV_lower, HSV_upper):

    hsv_f = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_f, HSV_lower, HSV_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contour = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    print contour

    #if len(contour) > 0:
        #c = max(contour,)

    return mask


def threshold(frame,HSV_lower, HSV_upper):

    lowerbound = np.array(HSV_lower)
    upperbound = np.array(HSV_upper)

    frame = cv2.inRange(frame, lowerbound, upperbound)

    return frame


def blob_handling(frame):

    params = cv2.SimpleBlobDetector_Params()

    #params.filterByColor = 1
    #params.blobColor = 255
    params.filterByArea = 1
    params.minArea = 500

    detector = cv2.SimpleBlobDetector_create(params)

    kernel = np.ones((7,7))
    frame = cv2.morphologyEx(frame,cv2.MORPH_CLOSE,kernel)

    keypoints = detector.detect(frame)

    print(keypoints)

    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    return im_with_keypoints


if __name__ == '__main__':

    capture = cv2.VideoCapture(1)

    while(True):
        ret, frame = capture.read()
        cv2.imshow('frame', frame)

        mask = detect_contours(frame, (0,0,0), (180,180,180))
        cv2.imshow('mask', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
