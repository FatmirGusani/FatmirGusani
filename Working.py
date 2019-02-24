import numpy as np
import cv2
#from picamera.array import PiRGBArray
#from picamera import PiCamera
#import time

# multiple cascades: https://github.com/Itsee/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter('Output.avi', fourcc, 20, (640,480))

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff

    
    #If key 'c' is pressed, it will take a picture.
    if k == ord("c"):
        cv2.imwrite('imsexy.png', img)
        
    
    #Record for 5 seconds
    if k == ord("r"):
        while (cap.isOpened()):
            ret, img = cap.read()
            if ret:
                video_writer.write(img)
                cv2.imshow('Video stream', img)
            else:
                break
        
    
    #Quit the "Frame"    
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
