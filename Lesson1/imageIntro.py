import cv2
import numpy as numpy
import matplotlib.pyplot as plt
#                               0
img = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCAHNGED = -1


#This will show using the CV method.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#This will show using matplotlib
##plt.imshow(img, cmap ='gray', interpolation='bicubic')
##plt.plot([50, 100], [80, 100], 'c', linewidth = 5)
##plt.show()

#This will write the CV output to a file
cv2.imwrite('examplegray.png', img)