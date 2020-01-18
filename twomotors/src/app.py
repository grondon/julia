from loadconf import config
import RPi.GPIO as GPIO
from input.KeyBoardHandler import KeyBoardHandler
#import time
from motors.RearWheelDrive import RearWheelDrive
from motors.SteeringWheel import SteeringWheel
#from input import read
from motors.Handler import Handler

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
# set GPIO Pins
GPIO.setwarnings(False)

#def test():  print("asdasd")
#read(test)


#handler = Handler(config) 
#handler.left()

handler = KeyBoardHandler(config)
handler.read()

#swheel = SteeringWheel(17)
#swheel.right()
