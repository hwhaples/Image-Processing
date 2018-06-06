import cv2
import numpy as np
import matplotlib.pyplot as plt

#This program demonstrates basic foreground extraction in openCV
#adjusting the value for rect will change the resulting foreground detection

img = cv2.imread('example.png')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

#sets the area of interest in a rectangle
rect = (75, 75, 300, 500)

#the following accomplishes the foreground extraction
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()