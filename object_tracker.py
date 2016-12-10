import cv2
import numpy as np

# TODO hsv is very noisy, maybe use RGB and a calibration mechanism?
# TODO increase robustness of primary blob


def threshold(frame,HSV_lower, HSV_upper):

    lowerbound = np.array(HSV_lower)
    upperbound = np.array(HSV_upper)

    frame = cv2.inRange(frame, lowerbound, upperbound)

    return frame

def blob_handling(frame):

    kernel = np.ones((3,3),np.uint8)

    filtered_frame = cv2.morphologyEx(frame,cv2.MORPH_OPEN,kernel)

    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 200
    params.maxThreshold = 255

    params.filterByArea = True
    params.minArea = 10

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(filtered_frame)

    if len(keypoints) != 0:

        key_X = int(keypoints[0].pt[0])
        key_Y = int(keypoints[0].pt[1])

        key_coords = (key_X,key_Y)
        return filtered_frame, key_coords

    else: return filtered_frame,()




if __name__ == '__main__':



    capture = cv2.VideoCapture(0)

    while(True):
        ret, frame = capture.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = threshold(hsv,[85, 20, 0],[100,255,255])

        blobim,centre_coord = blob_handling(mask)
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        hsv = cv2.bitwise_and(hsv,hsv,mask=blobim)

        cv2.imshow('frame',hsv)
        cv2.imshow('blobs',blobim)

        print(centre_coord)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
