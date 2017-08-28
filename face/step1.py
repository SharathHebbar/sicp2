import cv2
vc = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('/home/pi/Desktop/face/haarcascade_frontalface.xml')
# face detection with a rectangle

if vc.isOpened():
    ret, img = vc.read()
else:
    ret = False

while ret:
    cv2.imshow("preview", img)
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    key = cv2.waitKey(1)
    if key == 'q':
        break

cv2.destroyWindow("preview")
