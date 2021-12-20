#!/usr/bin/python

import threading
import time

def addlog():
	logpath = "/var/log/openerp-server/erp.log"

	megalog = "/var/log/erpmegalog/megalog.log"

	megalog_handler = open(megalog, "a+")
	logstring = ""

	for log in megalog_handler:
		logstring += log

	file_handler = open(logpath, "r")

	for line in file_handler:
		if line in logstring:
			print "line already exisits"
		else:
			megalog_handler.write(line+"\n")

	file_handler.close()
	megalog_handler.close()

while True:
	time.sleep(10)
	addlog()
