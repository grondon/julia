import RPi.GPIO as GPIO
import time
import sys
import select
#import tty
#import termios



import termios, fcntl, sys, os, select

fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = oldterm[:]
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        #r, w, e = select.select([fd], [], [])
        r = [fd]
        if r:
            c = sys.stdin.read(1)
            print "Got character", repr(c)
            if c == "q":
                break # quit
        print "counting" 
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)



