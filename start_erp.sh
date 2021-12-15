#!/bin/bash
echo "Checking OpenERP..."
a=`ps aux | grep '/usr/bin/python ./openerp-server.py --config=/etc/openerp-server.conf' | wc -l`

while true; do

	if [ "$a" -lt 2 ]; then
		echo "Restarting Openerp Server"
		/etc/init.d/openerp-server restart
	fi
	
	  sleep 5;

done
