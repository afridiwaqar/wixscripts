#!/bin/python

print "HELLO"


logpath = "/var/log/openerp-server/erp.log"
file_handler = open(logpath, "r")

substring = "successful login from"

for line in file_handler:
	if substring in line:
		print line
