#!/bin/bash

echo "Stop OpenERP"
/etc/init.d/openerp-server stop

echo 'Running Sync....'

rsync -acv --delete <username>@<IPADRESS>:/usr/local/lib/python2.7/dist-packages/openerp-server/addons/ /usr/local/lib/python2.7/dist-packages/openerp-server/addons

#echo $?

if [ "$?" =  0 ]; then
	echo "Replication performed successfully"
	echo "replication performed at $(date)" >> /home/username/replication_status
else
#	echo "$?"
	echo "ERROR ---> Problem with replication performed at $(date), rsync ended with exit code of $?" >> /home/username/replication_status
fi

echo "Starting OpenERP"
/etc/init.d/openerp-server start

echo 'all Done'
