#!/bin/bash

DB_USER=''
DB_NAME=''

LOCAL_BACKUP_DIR=/mnt/temp_local_db_backup

FILE_FILTER='prod-ss-db-backup-z-'
DATE_STR=$(date +'%Y-%m-%d_%H_%M_%S')

STATUS_FILE=/var/www/html/backuplog.html

echo "Dumping Database...Please wait"

pg_dump --host=<IPADDRESS> --port=5432 --username=$DB_USER --format=custom --file="${LOCAL_BACKUP_DIR}"/"${FILE_FILTER}""${DATE_STR}" --dbname=$DB_NAME --blob

if [ $? -eq 0 ]; then
	echo "<b>DB_Dump_Status:</b> Dump successful on $(date) <br />" >> $STATUS_FILE 
else
	echo "<b>DB_Dump_Status:</b> Dumping failed on $(date), exit status $? <br />"  >> $STATUS_FILE
fi

echo "Done Dumping Database..."

