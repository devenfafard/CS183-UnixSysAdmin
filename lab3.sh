#!/bin/bash

# REQUIREMENT 1
# find users in directory, owned by root, with setuid flagged, run ls with directory entries

find /usr/bin/ -user root -perm -4000 -exec ls -ldb {} \;
find /usr/sbin -user root -perm -4000 -exec ls -ldb {} \;

find /bin -user root -perm -4000 -exec ls -ldb {} \;
find /sbin -user root -perm -4000 -exec ls -ldb {} \;

# These files pose security risks because you can set them to run files owned by root
# ie. giving r/w permissions to the passwd file


# REQUIREMENT 2	

find / -perm -6000 -exec ls -ldb {} \;


# REQUIREMENT 3
# find files in var that have been modified in the last 20 minutes

find /var -cmin -20 -exec ls -ldb {} \;


# REQUIREMENT 4
# Find files in /var that are files with size 0

find /var -type f -size 0 -exec ls -ldb {} \;


# REQUIREMENT 5
# Find files in /dev that are not reg + not directories

find /dev ! -type d -exec ls -ldb {} \;


# REQUIREMENT 6
# Find all files in /home that are directories / not owned by root, chmod to 711

find /home -type d ! -user root -exec chmod 0711 {} \; 
find /home -type d ! -user root -exec ls -lbd {} \;


# REQUIREMENT 7
# Find regular files in home that are not owned by root, change permissions to 755

find /home -type f ! -user root -exec chmod 0755 {} \;
find /home -type f ! -user root -exec ls -lbd {} \;


# REQUIREMENT 8
# Find all files in /etc that have changed in the last 5 days

find /etc -type f -mntime 5
