from machine import UART, PWM, Pin
import time
import sdcard
from bno055 import *

"""
SUBSCALE PAYLOAD CONTROL Version 1.0-alpha
Author: Calista Greenway
Since: 11/09/2022
Created for University of Massachusetts Rocket Team (Payload Sub-Team)
This program collects and stores data from the BNO055 IMU, detects launch and landing, and orients to ground upon landing.
"""

# ---- INIT PHASE ----
### SD CARD
cs = machine.Pin(9, machine.Pin.OUT) # assign chip select (CS) pin

# intialize SPI peripheral
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(8))

sd = sdcard.SDCard(spi, cs) # initialize SD card

### IMU
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))
imu = BNO055(i2c)

### RADIO
baud_rates = [110,300,600,1200,2400,4800,9600,14400,19200,38400,57600,115200,128000,256000]
baud_rate_selection = 6 # to change baud rate

uart = UART(1, baud_rates[baud_rate_selection]) # setup uart object
uart.init(9600, parity=None, stop=1) # initialize the serial connection with given parameters
time.sleep(0.5)
uart.write('Initial Transmission - Rocket was connected to power') # How to send the message
time.sleep(0.5)

