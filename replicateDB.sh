#!/bin/bash

echo "Stop Postgresql"
/etc/init.d/postgresql stop

echo 'Running Sync....'

rsync -acv --delete username@<IPADRESS>:/var/lib/postgresql/<version>/main/ /var/lib/postgresql/<version>/main --exclude postmaster.pid --exclude pg_hba.conf --exclude recovery.done

if [ "$?" =  0 ]; then
#	echo "Database Replication performed successfully"
	echo "Database replication performed at $(date)" >> /home/<username>/replication_status
else
#	echo "$?"
	echo "ERROR ---> Problem with replication performed at $(date), rsync ended with exit code of $?" >> /home/USERNAME/replication_status
fi

echo "Starting Postgresql"
/etc/init.d/postgresql start

echo 'all Done'
