#!/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
from time import sleep
import RPi.GPIO as GPIO
#十六为3v3对面第八位
GPIO.setup(16, GPIO.OUT) #LED灯
GPIO.setup(11, GPIO.IN)  #开关位 
while 1:
      if GPIO.input(11):
         GPIO.output(16, False)
      else:
         GPIO.output(16,True)

