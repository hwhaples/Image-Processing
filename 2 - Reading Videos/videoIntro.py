import cv2
import numpy as np

#The parameter in videocapture refers to which webcam we will use
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
    if cv2.waitKey (1) && 0xFF == ord('q'):
        break

#These statements close any input
cap.release()
out.release()
cv2.destroyAllWindows()