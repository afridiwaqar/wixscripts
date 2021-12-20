#!/bin/bash

echo "Hello World..."

input_log="/var/log/openerp-server/erp.log"
output_log="/home/waqar/login_log.log"


while IFS= read line
do

#	echo "$line" | grep 'successful login from'
	log="$line" | grep 'successful login from'
	echo $log
	
	
done <"$input_log"

#cat /var/log/openerp-server/erp.log | grep 'successful login from'


