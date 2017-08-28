import os
import time


print "Image will be taken in 5 seconds."
time.sleep(5)
file_name="/home/pi/document-scanner/images/img.jpg"
cmd1= "raspistill -o "
cmd1+=file_name
os.system(cmd1)
time.sleep(5)

#cmd_mvr="mv "
#cmd_mvr+=file_name
#cmd_mvr+=" /home/pi/document-scanner/images"
#os.system(cmd_mvr)
#time.sleep(5)

#cmd_prog1="~/document-scanner"
#os.chdir("/home/pi/document-scanner")
#time.sleep(5)
cmd_prog="python scan_main.py --image images/img.jpg"
os.system(cmd_prog)
time.sleep(20)

