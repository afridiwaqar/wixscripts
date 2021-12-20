#!/bin/bash

DATE=`date +%Y-%m-%d`

echo "Rotating Log file and creating new one"
mv /var/log/erpmegalog/megalog.log /var/log/erpmegalog/'megalog.log_'$DATE
echo "Done"


