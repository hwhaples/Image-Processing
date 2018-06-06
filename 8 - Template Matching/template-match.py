import cv2
import numpy as np

#This example shows openCV's template matching ability.

img_example = cv2.imread('example.jpg')
img_gray = cv2.cvtColor(img_example, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.jpg', 0)
width, height = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8     #sets a threshold of match percentage

loc = np.where(res >= threshold)    #apply everywhere where the result > threshold for match

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_example, pt, (pt[0] + width, pt[1] + height), (0,255,255), 2)

cv2.imshow('Detected',img_example)