import cv2
import numpy as np

#This file is the same as filter1 and filter2, demonstrating morphological transformations
#such transformations can help further reduce noise from an input video.

cap = cv2.VideoCapture(0) #capture the webcam

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv = hue saturation value
    #here we set threshold values for the color of interest

    lower_color = np.array([160,150,0])
    upper_color = np.array([180,255,255])

    #now we will set a mask for the color
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask = mask) #masks the color on top of frame

    kernel = np.ones((5,5), np.uint8)

    #erosion and dilation use the local neighborhood to reduce input noise.
    #erosion erodes away, getting rid of external noise
    #dilation dilates, getting rid of internal noise
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    #opening and closing are morph transforms that further reduce noise
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    #show all the windows
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    #cv2.imshow('erosion', erosion)
    #cv2.imshow('dilation', dilation)
    #cv2.imshow('opening', opening)
    #cv2.imshow('closing', closing)

    if cv2.waitKey (5) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
