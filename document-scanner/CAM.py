import cv2

vc = cv2.VideoCapture(0)

sampleNum=0

if vc.isOpened():
    ret, img = vc.read()
else:
    ret = False

while(True):
    cv2.imshow("preview", img)
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("/home/pi/Desktop/document-scanner/fromcam/bizcard.jpg", gray)

    cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    
vc.release()
cv2.destroyAllWindows()

