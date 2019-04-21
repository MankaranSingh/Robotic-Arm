import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cv2.waitKey(1):

    _, frame = cap.read()
    blur = cv2.GaussianBlur(frame, (5,5), 0)
    
    hsv = cv2.cvtColor(blur, cv2.COLOR_RGB2HSV)
    
    lower_skin = np.array([110, 25, 85])
    upper_skin = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    blur = cv2.medianBlur(mask, 15)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
    hsv_d = cv2.dilate(blur, kernel)

    res = cv2.bitwise_and(frame,frame, mask= hsv_d)
##    hsv_d = cv2.resize(hsv_d, (64,48))

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',hsv_d)
    cv2.imshow('res',res)
    

cv2.destroyAllWindows()
cap.release()
