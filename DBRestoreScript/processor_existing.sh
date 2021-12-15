#!/bin/bash
USERNAME=""
IP_ADD=""
sshpass=""

set -- $(whoami)
USER=$1

latestDB=`ls /mnt/temp_local_db_backup/ -atr | tail -n 1`
echo "latest DB Selected" $latestDB

echo "Copying database to your home directory..."
echo "This might take forever, For the time being read the Torvolds cow special message for you..."

fortune | cowsay

sshpass -p "${sshpass}" scp -o StrictHostKeyChecking=no  /mnt/temp_local_db_backup/${latestDB} ${USERNAME}@${IP_ADD}:/home/${USERNAME}/

echo "Done Copying Database"
exit
