import cv2
import numpy as np

cap = cv2.VideoCapture(0) #capture the webcam

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv = hue saturation value
    #here we set threshold values for the color of interest

    lower_color = np.array([20,70,100])
    upper_color = np.array([50,200,130])

    #now we will set a mask for the color
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask = mask) #masks the color on top of frame

    #show all the windows
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    if cv2.waitKey (1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows
cap.release()
