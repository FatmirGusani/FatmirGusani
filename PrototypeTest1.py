# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#def Picture():
   # camera.start_preview()
    #sleep(5)
    #camera.cature('/home/pi/Desktop/image1.jpg')
def Record():
    camera.start_preview()
    camera.start_recording("/home/pi/video.h265")
    sleep(10)
    carmra.stop_recording()

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    
    #Takes Pictures
    if key == ord("c"):
        camera.start_preview()
        for i in range(2):
            time.sleep(2)
            camera.capture('/home/pi/Desktop/image%s.jpg' % i)
        camera.stop_preview()
    
    #Record for 5 seconds
    if key == ord("r"):
        camera.start_preview()
        for i in range(1):
            time.sleep(5)
            camera.start_recording('/home/pi/video%s.h264' % i)
        camera.stop_recording()
        camera.stop_preview()
    
    #Quit the "Frame"    
    if key == ord("q"):
        break
    
        
        
        
        
