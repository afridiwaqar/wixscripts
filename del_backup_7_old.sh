#!/bin/bash

echo 'finding backups older then a week...'

find /mnt/temp_local_db_backup/* -mtime +7

echo 'finding backups older then a week...'
#find /mnt/temp_local_db_backup/* -mtime +7 -exec rm {} \; # Delete backups Older then a month


echo "Current Year"
date +"%Y"
