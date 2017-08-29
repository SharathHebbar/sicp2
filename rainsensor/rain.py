import time
import RPi.GPIO as io

water_sensor = 18
io.setmode(io.BCM)
io.setup(water_sensor, io.IN)

n = 7
while n>1:
    read = io.input(water_sensor)
    n = n -1
    print read

    time.sleep(1)

io.cleanup()


