#!/usr/bin/python

import threading
import time

def checklogin():
	logpath = "/var/log/openerp-server/erp.log"

	substring = "successful login from"
	
	logpage = "/var/www/html/logins.html"
#	logpage = "login.html"
	
	logpage_handler = open(logpage, "a+")
	logstring = ""

#	logpage_11 = [x for x in logpage]
#	print logpage_11

	for log in logpage_handler:
		logstring += log

	file_handler = open(logpath, "r")

#	print "I am here"
	
	
	for line in file_handler:
		if substring in line:

			if line in logstring:
				print "line already exisits"
			else:
				logpage_handler.write(line+"</br></br>")
	
#	print "Hello again"

	file_handler.close()
	logpage_handler.close()

#try:
while True:
	time.sleep(10)
	checklogin()

#	threading.Timer(10, checklogin).start()
# except KeyboardInterrupt:
# 	threading.Timer.cancel()