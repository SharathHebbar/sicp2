import cv2
from picamera.array import PiRGBArray
vc = cv2.VideoCapture(0)
from picamera import PiCamera
import time
import numpy as np

# https://github.com/nazmiasri95/Face-Recognition/blob/master/face_recognition.py

camera = PiCamera()
camera.resolution = (320,240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))                        
display_window=cv2.namedWindow("Face")

face_cascade = cv2.CascadeClassifier('/home/pi/sicp2/face/haarcascade_frontalface.xml')

time.sleep(1)

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('/home/pi/sicp2/face/trainner/users.yml')



font = cv2.FONT_HERSHEY_SIMPLEX


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

        Id_predicted = recognizer.predict(gray_img[y:y+h,x:x+w])
       
        if(Id_predicted == 1):
            Id_predicted = "jo"
        elif(Id_predicted == 2):
            Id_predicted = "dk"
        elif(Id_predicted == 3):
            Id_predicted = "jk"
        else:
            Id_predicted = "unknown"
            
        cv2.putText(image, str(Id_predicted), (x,y+h),font, 2, (255,255,255), 3)
        
    cv2.imshow('Face',image)
    key = cv2.waitKey(1)
    
    rawCapture.truncate(0)

    if key == 27:
        camera.close()
        cv2.destroyAllWindows()
        break

