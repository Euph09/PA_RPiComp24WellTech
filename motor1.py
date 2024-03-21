import os
os.system("sudo pigpiod")
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

my_factory = PiGPIOFactory()
myGPIO =18
SERVO_DELAY_SEC = 0.01
myCorrection = 0.0
maxPW=(2.5+myCorrection)/1000
minPW=(0.5-myCorrection)/1000
servo = AngularServo(myGPIO, initial_angle=0, min_angle=0, max_angle=180, min_pulse_width=minPW, max_pulse_width=maxPW,pin_factory=my_factory)
        
def turn(fromAngle, toAngle):
	if fromAngle>toAngle:	#For closing vent
		for angle in range(fromAngle, toAngle, -1): #Smoothly turn from fromAngle to toAngle
			print("closing")
			servo.angle = angle
			time.sleep(SERVO_DELAY_SEC)
	else:
		for angle in range(fromAngle, toAngle, 1):	#For opening vent smoothly
			print("opening")
			servo.angle=angle
			time.sleep(SERVO_DELAY_SEC)
	log = open("PrevAngle","w")
	log.write(str(toAngle))
	log.close()

		
previousAngle = open("PrevAngle","r")	
	
previous = previousAngle.read()
previous = [int(i) for i in previous.split() if i.isdigit()]
previousAng = ''.join(str(e)for e in previous)

previousAngle.close()


toAngle = open("NewAngle","r")

to = toAngle.read()
to = [int(i) for i in to.split() if i.isdigit()]
toAng = ''.join(str(e)for e in to)

previousAngle.close()


turn(int(previousAng),int(toAng))
