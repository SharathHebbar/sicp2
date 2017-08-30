import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer()
cascPath = '/home/pi/sicp2/face/haarcascade_frontalface.xml'
detector = cv2.CascadeClassifier(cascPath)

def getImagesAndLabels(path):
    
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    
    faceSamples=[]

    Ids=[]
    
    for imagePath in imagePaths:

        pilImage=Image.open(imagePath).convert('L')
        
        imgnumpy=np.array(pilImage,'uint8')
        
        Id=int(os.path.split(imagePath)[-1].split(".")[1])

        faces=detector.detectMultiScale(imgnumpy)
        
        for (x,y,w,h) in faces:
            faceSamples.append(imgnumpy[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids

faces,Ids = getImagesAndLabels('/home/pi/sicp2/face/users/')
recognizer.train(faces, np.array(Ids))
recognizer.save('/home/pi/sicp2/face/trainner/users.yml')
