#https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
#Credits go to Marcelo Rovai (MJRoBot) for Real-Time Face Recognition: An End-to-End Project on February 23, 2018
#Fatmir Gusani And Sean Kelly
#Date : April 30, 2019

import cv2
import numpy as np
import time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
image_Counter = 0
video_Conuter = 0
imageName = 'Picture.jpg' #Just a random string
vidoName = 'outpy.avi'

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Fatmir', 'fatmir', 'Sean', 'sean', 'Leam', 'leam'] 
 
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

minW = 0.1*cap.get(3)
minH = 0.1*cap.get(4)
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(str(time.strftime("//home/pi/Desktop/Project/Video/Video-%Y_%m_%d_%H_%M_%S")) + '.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame_width,frame_height))
 
while(True):
  ret, frame = cap.read()

  frame = cv2.flip(frame, -1) # Flip vertically

  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
  for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            
        cv2.putText(frame, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(frame, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1) 
        #k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video


  if ret == True: 
     
    # Write the frame into the file 'output.avi'
    out.write(frame)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == ord('c' or 'C'):
      imageName = str(time.strftime("//home/pi/Desktop/Project/Picture/Picture-%Y_%m_%d_%H_%M_%S")) + '.jpg'
      cv2.imwrite(imageName, frame)

    # Display the resulting frame    
    cv2.imshow('frame',frame)

    if k == ord('q' or 'Q'):
     # Press Q on keyboard to stop recording
    #if cv2.waitKey(10) & 0xFF == ord('q' or 'Q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 
