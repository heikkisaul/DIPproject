import cv2
import numpy as np

def threshold(frame,BGR_lower, BGR_upper):

    lowerbound = np.array(BGR_lower)
    upperbound = np.array(BGR_upper)

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

        out_frame = blob_handling(threshold(frame,[0,0,150],[100,100,255]))

        cv2.imshow('blobim', out_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
