import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)



while True:
    ret,frame = cap.read()
    frame = cv.flip(frame,1)
    hsv_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_blue=np.array([100,150,0])
    upper_blue = np.array([120,255,255])
    blue_mask = cv.inRange(hsv_frame, lower_blue, upper_blue)
    green = cv.bitwise_and(frame,frame,mask=blue_mask)

    cv.imshow("Webcam", frame)
    cv.imshow("Blue ",green)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cv.destroyAllWindows()
