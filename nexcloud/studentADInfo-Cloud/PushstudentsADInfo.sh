#!/bin/bash

input="/home/waqar/Desktop/wixscripts/studentADInfo-Cloud/1.csv"

while IFS=',' read -r id name program username password

do 
	echo "Name: $name		Program: $program		Username: $username		Password: $password"
	export OC_PASS=$password
	echo $OC_PASS
	
	./occ user:add --password-from-env --display-name="$name" --group="student" --group="$program" "$username"

done < "$input"

