import cv2
import numpy as np

#This program will demonstrate OpenCV gradients and edge detection.

cap = cv2.VideoCapture(0) #capture webcam

while True:
    _, frame = cap.read() #allows editing of each frame of video

    #laplacian gradient
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    #we can also do gradients along the x or y dimensions with Sobel
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    #pure edge detection using Canny
    edges = cv2.Canny(frame, 100, 100)

    cv2.imshow('original', frame)
    #cv2.imshow('laplacian', laplacian)
    #cv2.imshow('sobelx', sobelx)
    #cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()