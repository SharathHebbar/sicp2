#main codes and configuration from:
#https://circuitdigest.com/microcontroller-projects/raspberry-pi-iot-intruder-alert-system

#added buzzer code from:
#https://circuitdigest.com/microcontroller-projects/raspberry-pi-motion-detector-pir-sensor

import RPi.GPIO as gpio
import picamera
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

fromaddr = "raspberrypi9648@gmail.com"
toaddr = "joanne9648@gmail.com"

mail = MIMEMultipart()

mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Alert!"
body = "Please check out the attachment"

#buzzer = 17
pir = 18

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
#gpio.setup(buzzer, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""

def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print data
    dat='%s.jpg'%data
    print dat
    attachment = open(dat, 'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "yonsei12345")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
    
def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(5)
    print data
    camera.capture('%s.jpg'%data)
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)
    
    
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55


while 1:
    if gpio.input(pir)==1:
        #gpio.output(buzzer, True)
        capture_image()
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        #gpio.output(buzzer, False)
        time.sleep(0.01)
        
