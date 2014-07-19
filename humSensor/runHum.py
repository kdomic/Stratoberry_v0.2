#!/usr/bin/python
import time
from time import gmtime, strftime
import datetime
import json
import signal
import sys
import ConfigParser
import Adafruit_DHT

run = True

def signal_handler(signal, frame):
	run = False
	print('\nEND\n')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

config = ConfigParser.RawConfigParser()
config.read('/home/stratoberry/settings.cfg')
storeLocation = config.get('Hum', 'storeLocation')
refreshTime = config.getint('Hum', 'refreshTime')
showOutput = config.getboolean('Hum', 'showOutput')

while run:
	dict = {}
	timeNow = strftime("%Y%m%d%H%M%S", time.localtime())		
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
	if humidity is not None and temperature is not None:
		temp = '{0:0.2f}'.format(temperature)
		hum = '{0:0.1f}'.format(humidity)
		dict[timeNow] = [temp, hum] 
		open(storeLocation+timeNow+".json","w").write(json.dumps(dict, sort_keys=True))
		if showOutput:
			print 'Temp={0:0.2f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	else:
		if showOutput:
			print 'Failed to get reading. Try again!'
	time.sleep(refreshTime)
