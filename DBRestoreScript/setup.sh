#!/bin/bash

echo "Setting up your database restore script, please wait"
echo
echo "Setting IP Address...."
echo
IP_ADD="$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')"
sed -i 's/^\(IP_ADD=\).*/\1\"'$IP_ADD'"/' processor_existing.sh
sed -i 's/^\(IP_ADD=\).*/\1\"'$IP_ADD'"/' processor_latest.sh

echo "Setting Username...."
echo
USERNAME=$(whoami)
sed -i 's/^\(USERNAME=\).*/\1\"'$USERNAME'"/' processor_existing.sh
sed -i 's/^\(USERNAME=\).*/\1\"'$USERNAME'"/' processor_latest.sh

echo "Enter your password"
#read SSHPASS

unset SSHPASS;
while IFS= read -r -s -n1 pass; do
  if [[ -z $pass ]]; then
     echo
     break
  else
     echo -n '*'
     SSHPASS+=$pass
  fi
done

sed -i 's/^\(sshpass=\).*/\1\"'$SSHPASS'"/' processor_existing.sh
sed -i 's/^\(sshpass=\).*/\1\"'$SSHPASS'"/'  processor_latest.sh
echo
echo "Fetching list of DataBase users..."
echo
psql -U postgres -d cms -c "SELECT rolname FROM pg_roles;"

echo "Enter the name of your database user"
read DBUSER

sed -i 's/^\(DBUSER=\).*/\1\"'$DBUSER'"/' get-latest-db.sh
#sed -i 's/^\(DBUSER=\).*/\1$DBUSER/' processor_latest.sh
echo
echo "Done setting up configurations"
echo
echo "To get a copy of the database, run ./get-latest-db.sh"
echo
echo "To get the lastest database to this moment, run ./get-latest-db.sh -l (slow)"
echo

