from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.resolution = "2592x1944"
camera.sharpness = 100
camera.IMAGE_EFFECTS('negative')
camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

