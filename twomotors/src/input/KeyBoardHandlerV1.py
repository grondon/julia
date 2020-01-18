import RPi.GPIO as GPIO
#import time
import sys
#import select
#import tty
#import termios

from motors.Handler import Handler
from sensors.Distance import HCSR04

class KeyBoardHandler:


     def __init__(self,config):
         self.handler = Handler(config)
         #self.hcsr04 = HCSR04(25,18)

     #def isData(self):
     #    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

     def read(self):
       while True:
         action = raw_input ("Enter your name: ")
         self.action(action)
         if(action == 'q'):
           exit() 


     def read2(self):
         old_settings = termios.tcgetattr(sys.stdin)
         try:
            tty.setcbreak(sys.stdin.fileno())
            while 1:
            # print(i)
               if self.isData():
                   c = sys.stdin.read(1)
                   if c == '\x1b':         # x1b is ESC
                      break
                   self.action(c)
               #print(self.hcsr04.distance())

               #time.sleep(0.3)
               #if(self.hcsr04.distance()<=15):
               #    self.action('o')
         finally:
             termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

     def action(self,action):
        print(action)
        {
             'a': self.handler.left,
             's': self.handler.center,
             'd': self.handler.right,
             'i': self.handler.foward,
             'o': self.handler.stop,
             'p': self.handler.back
         }[action]()
