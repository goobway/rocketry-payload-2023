import machine
import time
import sdcard
import uos
from bno055 import *

"""
IMU DATA COLLECTION Version 0.9-alpha
Author: Calista Greenway
Since: 11/03/2022
Created for University of Massachusetts Rocket Team (Payload Sub-Team)
This program collects and stores data from the BNO055 interial measurement unit to an SD card.
"""

"""
SD CARD SETUP
"""
# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(9, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(8))

# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")


"""
BNO055 SETUP
"""
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
imu = BNO055(i2c)

"""
WRITE TO SD CARD CSV FILE
"""

# Create a file and write something to it
with open("/sd/test01.txt", "w") as file:
    file.write("Hello, SD World!\r\n")
    file.write("This is a test\r\n")
    
    file.write('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))
    file.write('Temperature {}°C'.format(imu.temperature()))
    file.write('Mag       x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.mag()))
    file.write('Gyro      x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.gyro()))
    file.write('Accel     x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.accel()))
    file.write('Lin acc.  x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.lin_acc()))
    file.write('Gravity   x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.gravity()))
    file.write('Heading     {:4.0f} roll {:4.0f} pitch {:4.0f}'.format(*imu.euler()))

