from machine import Pin, PWM
from time import sleep
import time
import utime
from bno055 import *

i2c = machine.I2C(0, sda = machine.Pin(16), scl = machine.Pin(17))
imu = BNO055(i2c)

servo = PWM(Pin(19))
servo.freq(50)

servoStop = 1500
servoCCW = 1000000
servoCW = 2000000
print("CCW")
servo.duty_ns(servoCCW)
utime.sleep(2)
print("STOP")
servo.duty_ns(servoStop)
utime.sleep(2)

acc = imu.accel()

while acc[2] < 9.6:
    acc = imu.accel()
    print(acc[2])
    print("not level yet...")
    servo.duty_u16(1000)
    sleep(0.01)
    #for position in range(1000, 9000, 500):
        #print(position)
        #pwm.duty_u16(position)
        #sleep(0.01)
        
print("found!")
    
'''
while True:
    for position in range(1000, 9000, 50): # position 1000 = 0 degrees and position 9000 = 180 degrees
        pwm.duty_u16(position)
        sleep(0.01)
    for position in range(9000, 1000, -50):
        pwm.duty_u16(position)
        sleep(0.01)
'''