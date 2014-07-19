#!/usr/bin/python
import Adafruit_BMP.BMP085 as BMP085
import time
from time import gmtime, strftime
import datetime
import json
import signal
import sys
import ConfigParser

#import RPi.GPIO as GPIO ## Import GPIO library
#GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
#GPIO.setwarnings(False)
#GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
#ledStatus = True

sensor = BMP085.BMP085()
run = True

def signal_handler(signal, frame):
	run = False
	print('\nEND\n')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

config = ConfigParser.RawConfigParser()
config.read('/home/stratoberry/settings.cfg')
storeLocation = config.get('Temp', 'storeLocation')
refreshTime = config.getint('Temp', 'refreshTime')
showOutput = config.getboolean('Temp', 'showOutput')

while run:
	
#	GPIO.output(7,ledStatus) ## Turn on GPIO pin 7
#	if ledStatus:
#		ledStatus = False
#	else:
#		ledStatus = True
	
	dict = {}
	timeNow = strftime("%Y%m%d%H%M%S", time.localtime())	
	temp = '{0:0.2f}'.format(sensor.read_temperature())
	pressure = '{0:0.2f}'.format(sensor.read_pressure())
	altitude = '{0:0.2f}'.format(sensor.read_altitude())
	sea = '{0:0.2f}'.format(sensor.read_sealevel_pressure())
			
	dict[timeNow] = [temp, pressure, altitude, sea] 
	open(storeLocation+timeNow+".json","w").write(json.dumps(dict, sort_keys=True))
	
	if showOutput:
		print timeNow + "\nTemp = " + temp + "\nPressure = " + pressure + "\nAltitude = " + altitude + "\nSealevel Pressure = " + sea + "\n\n"
	
	time.sleep(refreshTime)
