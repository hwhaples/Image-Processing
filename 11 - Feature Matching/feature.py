import cv2
import numpy as np
import matplotlib.pyplot as plt

#note, this is a brute force algorithm to feature match compare

img1 = cv2.imread('template.jpg', 0)
img2 = cv2.imread('example.jpg', 0)

orb = cv2.ORB_create()

keyPoint1, des1 = orb.detectAndCompute(img1, None)
keyPoint2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, keyPoint1, img2, keyPoint2, matches[:10], None, flags = 2)
plt.imshow(img3)
plt.show()