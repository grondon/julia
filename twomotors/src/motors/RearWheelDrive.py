import RPi.GPIO as GPIO

class RearWheelDrive:

   def __init__(self, gpioA,gpioB):
       self.gpioA = gpioA
       self.gpioB = gpioB
       GPIO.setup(gpioA, GPIO.OUT)
       GPIO.setup(gpioB, GPIO.OUT)

   def foward(self):
       GPIO.output(self.gpioA, GPIO.HIGH)
       GPIO.output(self.gpioB, GPIO.LOW)

   def stop(self):
       GPIO.output(self.gpioA, GPIO.LOW)
       GPIO.output(self.gpioB, GPIO.LOW)

   def back(self):
       GPIO.output(self.gpioA, GPIO.LOW)
       GPIO.output(self.gpioB, GPIO.HIGH)


