import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
camera.start_recording('examplevid2.h264')
time.sleep(10)
camera.stop_recording
