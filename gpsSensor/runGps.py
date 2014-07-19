#! /usr/bin/python
# coding=utf-8

import os
from gps import *
from time import *
import time
import datetime
import threading
#import socket
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/stratoberry/settings.cfg')
storeLocation = config.get('GPS', 'storeLocation')
currentStoreFolder = strftime("%Y%m%d%H%M%S/", time.localtime())
refreshTime = config.getint('GPS', 'refreshTime')
showOutput = config.getboolean('GPS', 'showOutput')

os.makedirs(storeLocation+currentStoreFolder)

time.sleep(5)

#if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(('127.0.0.1',2947)) != 0:
#	os.system('gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock')

gpsd = None
if showOutput: os.system('clear')

class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd
		gpsd = gps(mode=WATCH_ENABLE)
		self.current_value = None
		self.running = True
	def run(self):
		global gpsd
		while gpsp.running:
			gpsd.next()

if __name__ == '__main__':
	gpsp = GpsPoller()
	try:
		gpsp.start()
		time.sleep(5)
		while True:
			dict = {}
			timeNow = strftime("%Y%m%d%H%M%S", time.localtime())
			dict[timeNow] = [gpsd.fix.latitude,
								gpsd.fix.longitude,
								gpsd.utc,
								gpsd.fix.time,
								gpsd.fix.altitude,
								gpsd.fix.eps,
								gpsd.fix.epx,
								gpsd.fix.epv,
								gpsd.fix.ept,
								gpsd.fix.speed,
								gpsd.fix.climb,
								gpsd.fix.track,
								gpsd.fix.mode
							] 
			open(storeLocation+currentStoreFolder+timeNow+".json","w").write(json.dumps(dict, sort_keys=True))
			
			if showOutput:
				os.system('clear')
				print
				print ' GPS reading'
				print '----------------------------------------'
				print 'latitude    ' , gpsd.fix.latitude
				print 'longitude   ' , gpsd.fix.longitude
				print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
				print 'altitude (m)' , gpsd.fix.altitude
				print 'eps		   ' , gpsd.fix.eps
				print 'epx		   ' , gpsd.fix.epx
				print 'epv		   ' , gpsd.fix.epv
				print 'ept		   ' , gpsd.fix.ept
				print 'speed (m/s) ' , gpsd.fix.speed
				print 'climb		 ' , gpsd.fix.climb
				print 'track		 ' , gpsd.fix.track
				print 'mode		  ' , gpsd.fix.mode
				print
				print 'sats		  ' , gpsd.satellites
			time.sleep(refreshTime) #set to whatever
	except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
		if showOutput:
			print "\nKilling Thread..."
		gpsp.running = False
		gpsp.join() # wait for the thread to finish what it's doing

if showOutput:
	print "Done.\nExiting."
