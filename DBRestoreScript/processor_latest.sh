#!/bin/bash
USERNAME=""
sshpass=""
SRV_DBUSER=""
SRV_USERNAME=''
SRV_IP_ADD=''
DB=""
IP_ADD="$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')"
sed -i 's/^\(IP_ADD=\).*/\1\"'$IP_ADD'"/' processor_latest.sh

set -- $(whoami)
USER=$1

echo "Backing up database..."
echo "This will take some time, so for time being read this to kill some time..."
#echo $USER

if [ -d "${USERNAME}" ]; then
  rm -rf /home/${USER}/${USERNAME}/
fi

fortune | cowsay
mkdir /home/${USER}/${USERNAME}

sudo pg_dump --host=<IPADDRESS> --port=5432 --username="openerp" --format=custom --file="/home/${USER}/${USERNAME}/prod-ss-db-backup-z-Latest" --dbname="${DB}" --blob

echo "Copying database to your home directory..."
echo "This might take forever, For the time being read the Torvolds cow special message for you..."

fortune | cowsay

sshpass -p "${sshpass}" scp -o StrictHostKeyChecking=no /home/${USER}/${USERNAME}/prod-ss-db-backup-z-Latest ${USERNAME}@${IP_ADD}:/home/${USERNAME}/
rm -rf /home/${USER}/${USERNAME}/

echo "Done Copying Database"
exit

