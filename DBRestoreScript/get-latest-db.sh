#!/bin/bash

SRV_USERNAME=''
SRV_IP_ADD=''
DB=""

if [ "$1" == "-l" ]; then
	echo "Getting the Latest Database"
	echo "Logging in to Server"
	ssh ${SRV_USERNAME}@${SRV_IP_ADD} 'bash -s' < processor_latest.sh

else
	echo "Logging in to Server"
	ssh ${SRV_USERNAME}@${SRV_IP_ADD} 'bash -s' < processor_existing.sh
fi

echo "Restoring Database...."

echo "Terminating Existing Connections...."

pkill pgadmin
psql -U postgres -d cms -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'cms' AND pid <> pg_backend_pid()"

echo "Deleting Old Databse..."
psql -U postgres -c "drop database cms"

set -- $(whoami)
USER=$1

echo "Creating New cms Database for ${DBUSER}"
psql -U postgres -c "CREATE DATABASE cms OWNER ${DBUSER}"

latest_DB=`ls /home/${USER}/prod* -Art | tail -n 1`

echo "Latest DB" ${latest_DB}

echo "Restore the latest Backup"
/usr/bin/pg_restore --host <IPADDRESS> --port 5432 --username "${DBUSER}" --dbname $DB --no-password --verbose "${latest_DB}"

rm ${latest_DB}

echo "Stopping all Cron Jobs"
psql -U postgres -d $DB -c "update ir_cron set active = False"

echo "Setting Simplied password for Admin aaa "
psql -U postgres -d $DB -c "update res_users set password = 'aaa' where login='admin'"

echo "All Dones"
