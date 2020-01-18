import RPi.GPIO as GPIO
import time


class HCSR04:

    def __init__(self,pinTrigger,pinEcho):
        self.pinTrigger = pinTrigger
        self.pinEcho = pinEcho


    def  distance(self):

        try:
            start = 0
            recive=0
            GPIO.setup(self.pinTrigger, GPIO.OUT)
            GPIO.setup(self.pinEcho, GPIO.IN)
            # set Trigger to HIGH
            GPIO.output(self.pinTrigger, True)
            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(self.pinTrigger, False)

            startTime = stopTime  = time.time()
            # save start time
            while 0 == GPIO.input(self.pinEcho):
                #startTime = time.time()
                start = start +1
            startTime = time.time()
            # save time of arrival
            while 1 == GPIO.input(self.pinEcho):
                #stopTime = time.time()
                recive =  recive +1
            stopTime = time.time()

            # time difference between start and arrival
            TimeElapsed = stopTime - startTime
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance = (TimeElapsed * 34300) / 2
            print ("Distance: %.1f cm" % distance)
            time.sleep(0.05)
            return distance
            #print(start)
            #print(recive)
            #print("===============")
            #return distance
        except Exception as e:
            print ("ocurrio un error" + str(e))
            return -1
