import cv2
import numpy as np

#This file is the same as filter 1, but demonsrates various blurs to help get rid of noise

cap = cv2.VideoCapture(0) #capture the webcam

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv = hue saturation value
    #here we set threshold values for the color of interest

    lower_color = np.array([20,70,100])
    upper_color = np.array([100,255,255])

    #now we will set a mask for the color
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask = mask) #masks the color on top of frame

    #first is an average blur
    kernal = np.ones((15,15), np.float32)/(15*15)
    smoothed = cv2.filter2D(res, -1, kernal)

    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)


    #show all the windows
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    if cv2.waitKey (5) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
