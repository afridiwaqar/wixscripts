#!/bin/bash

orig_user=$(whoami)
if [[ $orig_user = openerp ]]
then
	echo "Restarting OpenERP Server by Force..."

	if [ ! -f /var/run/openerp-server.pid ]; then
		sudo touch /var/run/openerp-server.pid
		sudo chown  openerp.root /var/run/openerp-server.pid
		/etc/init.d/openerp-server restart
	else
		/etc/init.d/openerp-server restart
	fi

else
	echo "Wrong User: Switch to Openerp User"	
fi

