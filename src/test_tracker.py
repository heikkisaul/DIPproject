import cv2

def detect_contours(frame, HSV_lower, HSV_upper):

    hsv_f = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv_f = cv2.GaussianBlur(hsv_f, (11, 11), 0)

    mask = cv2.inRange(hsv_f, HSV_lower, HSV_upper)

    contour = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(contour) > 0:
        c = max(contour,key=cv2.contourArea)
        #((x,y),radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if int(M["m00"]) <= 100:
            center = None
        else:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]) )

        #cv2.circle(mask, center, 5, (0, 0, 255), -1)

        print(M["m00"])

    return center, mask

if __name__ == '__main__':

    capture = cv2.VideoCapture(0)

    while(True):
        ret, frame = capture.read()
        cv2.imshow('frame', frame)

        center,mask = detect_contours(frame, (30,50,50), (40,255,255))

        print(center)
        cv2.imshow('mask', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
