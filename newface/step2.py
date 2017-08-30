from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))

face_cascade = cv2.CascadeClassifier('/home/pi/sicp2/face/haarcascade_frontalface.xml')

Id=raw_input('enter your id: ')
sampleNum=0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    #FACE DETECTION STUFF
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("/home/pi/sicp2/face/users/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

    cv2.imshow('frame',image)
    
    #DISPLAY TO WINDOW
    key = cv2.waitKey(1)
    rawCapture.truncate(0)
    #incrementing sample number 
    if cv2.waitKey(10) & 0xFF == ord('q'):
        camera.close()
        cv2.destroyAllWindows()
        break
    # break if the sample number is morethan 20
    elif sampleNum>19:
        camera.close()
        cv2.destroyAllWindows()
        break
