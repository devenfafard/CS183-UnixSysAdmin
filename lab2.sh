#!/usr/bin/bash

awk -F ":" '{ print $4":"$1 }' /etc/passwd > users.txt
awk -F ":" '{ print $3":"$1 }' /etc/group > groups.txt

awk -F ":" 'NR==FNR{a[$1]=$1":"$2; next} {$1 in a}{print $2":"a[$1]}' groups.txt users.txt

