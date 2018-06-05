import numpy as np
import cv2

img = cv2.imread('example.jpg', cv2.IMREAD_COLOR)

#In this code we will isolate a region of interest and copy it back to the same region

img[55,55] = [255,255,255] #changes the (55,55) pixel to white
px = img[55,55]

img[100:500, 100:500] = [255,255,255] #sets region to white


#sets the corner to be a copy of region of interest
location = img[37:111, 107:194]
img[0:74, 0:87] = location

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()