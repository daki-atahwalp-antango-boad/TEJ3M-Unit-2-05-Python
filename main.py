# Created by: Daki A.B
# Created on: April 2025
#
# This program turns a servo from 0 to 180 degrees and repeats

import time
import board
import pwmio
from adafruit_motor import servo

# constants
TURN_TIME = 0.05

# creating a PWMOut object on Pin GP7.
pwm = pwmio.PWMOut(board.GP7, duty_cycle=2 ** 15, frequency=50)

# Creating a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees each time.
        my_servo.angle = angle
        time.sleep(SLEEP_TIME)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees each time.
        my_servo.angle = angle
        time.sleep(SLEEP_TIME)
