import cv2
import numpy as np

# https://github.com/nazmiasri95/Face-Recognition/blob/master/face_recognition.py

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('/home/pi/Desktop/face/trainner/users.yml')
cascPath = '/home/pi/Desktop/face/haarcascade_frontalface.xml'

faceCascade = cv2.CascadeClassifier(cascPath)

font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

while True:
    ret, img =cam.read()
    
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=faceCascade.detectMultiScale(gray_img, 1.2, 5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),4)
        
        Id_predicted = recognizer.predict(gray_img[y:y+h,x:x+w])
       
        if(Id_predicted == 1):
            Id_predicted = "dk"
        elif(Id_predicted == 2):
            Id_predicted = "kee"
        elif(Id_predicted == 3):
            Id_predicted = "jo"
        else:
            Id_predicted = "unknown"
            
        cv2.putText(img, str(Id_predicted), (x,y+h),font, 2, (255,255,255), 3)
        
    cv2.imshow('img',img)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

