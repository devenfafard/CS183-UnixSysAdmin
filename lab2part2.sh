#!/usr/bin/bash

if [ -f "lab2-test.txt" ];
then
     echo "$(date +%D-%T) -File "/LinuxSysAdmin/lab2-test.txt" has been found. " > ../../var/log/cs183/uptime.log
     grep "lost" ../../var/log/cs183/uptime.log | tail -1 && echo "$(date +%D-%T) -File "/LinuxSysAdmin/lab2-test.txt" has been found. " 
else
     echo "$(date +%D-%T) -File "/LinuxSysAdmin/lab2-test.txt" has been lost. " > ../../var/log/cs183/uptime.log
     grep "found" ../../var/log/cs183/uptime.log | tail -1 && echo "$(date +%D-%T) -File "/LinuxSysAdmin/lab2-test.txt" has been found."
fi
