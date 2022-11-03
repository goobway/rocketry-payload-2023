# Program for operating the BNO055

import machine
import time
from adafruit_bno055 import *

# Pyboard hardware I2C
i2c = machine.I2C(1)

imu = BNO055(i2c)

