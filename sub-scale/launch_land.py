import machine
import time
import math
from collections import deque
from bno055 import *

i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
imu = BNO055(i2c)

# Launch Detection
launch_flag = False

# test = deque()

while launch_flag == False:
    acc = imu.lin_acc()                                   # acceleration vector
    accMag = math.sqrt(acc[0]**2 + acc[1]**2 + acc[2]**2) # acceleration magnitude
    
    print(accMag)
    
    startTime = time.time()
    while accMag >= (9.8*1.05):
        print(accMag)
        endTime = time.time()
        print("Holding...")
        if (endTime - startTime > 2):
            launch_flag = True

print("Launch Detected!")

# Landing Detection
