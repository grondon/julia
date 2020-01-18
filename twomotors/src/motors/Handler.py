from loadconf import config
import RPi.GPIO as GPIO
import time
from motors.RearWheelDrive import RearWheelDrive
from motors.SteeringWheel import SteeringWheel 


class Handler:

  def __init__(self,config):
     self.rearwheel = RearWheelDrive(config["motors"]["gpio1A"],config["motors"]["gpio1B"])
     self.steeringwheel =  SteeringWheel(config["servos"]["gpioA"])

  def left(self):
     self.steeringwheel.left()

  def right(self):
     self.steeringwheel.right()

  def center(self):
    self.steeringwheel.center()

  def foward(self):
    self.rearwheel.foward()

  def stop(self):
    self.rearwheel.stop()

  def back(self):
    self.rearwheel.back()

