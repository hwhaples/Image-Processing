import cv2
import numpy as np

#This code will showcase openCV's ability to do arithmetic operations, the images are the same size

img1 = cv2.imread('first-image.png')
img2 = cv2.imread('second-image.jpg')
img3 = cv2.imread('logo.png')

#add = img1 + img2 This will do a rough add, imshow to see
#add = cv2.add(img1, img2) This will do a straight add of pixel values, mainly wight output
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) This will do a weighted add of two images

rows,cols,channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

#The following line will:
#If a pixel is above 220, it will be 255, if below it is black
#Then it will make it black. 
ret, mask = cv2.threshold(img3gray, 246, 255, cv2.THRESH_BINARY_INV)

#bitwise is a lowlevel logical operation like python logical operation
#so we will select the part of image that we want

mask_inv = cv2.bitwise_not(mask) 

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg) #combined image1's background with img3's foreground
img1[0:rows, 0:cols] = dst      #sets image to place.


#cv2.imshow('mask', mask)
cv2.imshow('combined', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()