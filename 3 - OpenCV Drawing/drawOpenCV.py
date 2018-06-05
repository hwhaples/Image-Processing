import numpy as np
import cv2

#this file shows the image drawing capabilities of the OpenCV drawing.

img = cv2.imread('example.jpg', cv2.IMREAD_COLOR)

#cv2.shape(photo, start(0,0), finish(0.0), color(B,G,R), thickness)

cv2.line(img, (10,10), (200,150), (0,255,0), 5)
cv2.rectangle(img, (100,63), (200,150), (255,255,255), 15)

#circle uses center, radius. -1 means that color will fill the shape.
cv2.circle(img, (50,50), 90, (0,0,255), -1)

#how to create a poly-line structure

pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
#'True' refers to whether or not the polyline is closed
cv2.polylines(img, [pts], True, (255,255,0), 5)

#how to insert
#cv2.Line_AA accomplishes line anti-aliasing
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello World', (0,200), font, 1, (240, 34, 251), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()