import RPi.GPIO as GPIO
import time


class SteeringWheel:

   LEFT = 1
   RIGHT = 10
   CENTER = 5
   STEP = 1

   def __init__(self,gpio):
      self.gpioA = gpio
      GPIO.setup(self.gpioA, GPIO.OUT)
      #self.position = 7;
      self.p = GPIO.PWM(self.gpioA, 50) # GPIO 17 for PWM with 50Hz
      self.p.start(0) # Initialization
      self.current = self.CENTER
      print("constructor")
      #self.p.ChangeDutyCycle(self.CENTER)
      #time.sleep(0.2)
      #self.p.ChangeDutyCycle(0)
      #time.sleep(0.2)
      #print ("asdasd")

   def center(self):
      #self.turn(self.CENTER)
         self.p.ChangeDutyCycle(self.CENTER)
         time.sleep(0.2)
         self.p.ChangeDutyCycle(0)
         time.sleep(0.2)
         self.current=self.CENTER

   def right(self):
      print("position right:"+str(self.current)+"<"+str(self.RIGHT))
      if(self.current<self.RIGHT):
         self.turn(1)
      #self.p.ChangeDutyCycle(7)
      #time.sleep(0.2)
      #self.p.ChangeDutyCycle(0)
      #time.sleep(0.2)
      #self.current=self.CENTER


   def left(self):
      print("position left:"+str(self.current)+">"+str(self.LEFT))
      if(self.current>self.LEFT):
        self.turn(-1)

   def turn(self,step):
         self.current = self.current+step
         #print("UPDTE:"+str(self.current))
         self.p.ChangeDutyCycle(self.current)
         time.sleep(0.2)
         self.p.ChangeDutyCycle(0)
         #time.sleep(0.2)
         #print("position:"+str(self.current))


#GPIO.setmode(GPIO.BCM)
#xx = SteeringWheel(17)
#xx.right()
#xx.left()
