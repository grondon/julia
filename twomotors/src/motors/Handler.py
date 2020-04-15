from loadconf import config
import RPi.GPIO as GPIO
import time
from motors.RearWheelDrive import RearWheelDrive
from motors.SteeringWheel import SteeringWheel 


class Handler:

  def __init__(self,config):
     self.rearwheelA = RearWheelDrive(config["motors"]["gpio1A"],config["motors"]["gpio1B"])
     self.rearwheelB = RearWheelDrive(config["motors"]["gpio2A"],config["motors"]["gpio2B"])
     #self.steeringwheel =  SteeringWheel(config["servos"]["gpioA"])

  def left(self):
     self.rearwheelA.foward() 
     self.rearwheelB.back()

  def right(self):
     self.rearwheelB.foward() 
     self.rearwheelA.back()

  def center(self):
    self.rearwheelA.stop()
    self.rearwheelB.stop()

  def foward(self):
    self.rearwheelA.foward()
    self.rearwheelB.foward()

  def stop(self):
    self.rearwheelA.stop()
    self.rearwheelB.stop()

  def back(self):
    self.rearwheelA.back()
    self.rearwheelB.back()

