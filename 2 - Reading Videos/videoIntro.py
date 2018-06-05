import cv2
import numpy as np

#This file opens up 2 video streams, one in color and one gray.
#It then saves the capture to output.avi on the press of 'q'

#The parameter in videocapture refers to which webcam we will use 
#Replacing the parameter with a file name will allow us to use prerecorded video
cap = cv2.VideoCapture(0)

#Video Codec and saving requirements
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#This loop controls video capture
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    #break the loop if the q key is pressed
    if cv2.waitKey (1) & 0xFF == ord('q'):
        break

#These statements close any input
cap.release()
out.release()
cv2.destroyAllWindows()