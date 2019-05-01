#!/bin/bash

echo "########## DD ##########"
# 'dd' is used to convert and copy files, generally w/ resepect to hard drives.
# It can also be used for more advanced I/O. This can be useful when needing to 
# skip certain parts of a script to run it on another machine.

# This command creates a disk img of a hard drive mounted at /dev/hda.

# dd if=/dev/hda of=~/currentdisk.img

# This command skips the first 4 bytes of a file and outputs it to another file.
# file1.txt="hey, what's up?" file2.txt=" what's up?"

dd if=file1.txt of=file2.txt ibs=4 skip=1
cat file2.txt

read -p "Hit any key to continue."

###############################################################################
echo "########## FIND ##########"
# 'find' is used to look for files meeting any number of criteria. The results 
# can then be piped to different functions for further use. A useful scenario 
# is if you discover your system has been breached, but you do not know the 
# source of the breach / what files have been compromised. You can then search 
# the entire system for files that have been changed recently or that had their 
# permissions changed. It's also useful for finding zombie processes.

# This command finds files across the entire system that have been modified in 
# the last 5 days and have had setuid & setgid changed. Should only return any
# zombie processes still floating around.

find / -perm /6000 -mtime 5 -exec ls -ldb {} \;

read -p "Hit any key to continue."

##############################################################################
echo "########## FILE ##########"
# 'file' is used to view file types. It will return the file type of a given
# file. It can be useful because file names are entirely independent of the 
# file type.

# This command looks into gzip files matching the pattern "file*.txt" to see 
# what uncompressed files they contain.

file -z file*.txt.gz

read -p "Hit any key to continue."

#############################################################################
echo "######### FUSER ##########"
# 'fuser' is used to see which process is using a file. This can be useful
# when debugging rogue processes or ensuring manipulating a file won't cause
# havoc on a process.

# This command lists the processes that are being run by the current user.
# '-v' puts it in verbose mode which prints the output to the screen. 
fuser -v .

read -p "Hit any key to continue."

#############################################################################
echo "########## GREP ##########"
# 'grep' searches input files for patterns or exact strings given by the user.
# By default it copies matched lines to stdout. It's useful for searching
# long files, like /etc/passwd.

# This command searches /etc/passwd for lines that contain 'root'.

grep root /etc/passwd

read -p "Hit any key to continue."

############################################################################
echo "########## HOST ###########"
# 'host' is used to convert IP addresses to names and vice versa. This can
# be useful when needing to interface with another host machine and can be
# used to verify IP addresses before data is transferred.

# This command performs a DNS lookup for 204.228.150.3.

host 204.228.150.3

read -p "Hit any key to continue."

############################################################################
echo "########## LDD ##########"
# 'ldd' is used to list shared libraries required by an executable file.
# This can be useful when upgrading software, to check what dependencies
# an install may have before removing or installing a new version.

# This command should indicate that this executable file is not dynamically
# executable (ie. has no dependent libraries like a .c, .elf, or .hex file
# would have).

ldd -v hw2.sh

read -p "Hit any key to continue."

############################################################################
echo "########## LSOF ##########"
# 'lsof' is used to list all open files by each process. This can be useful 
# when trying to kill processes. You can use this command to see if any 
# essential files are open before you kill it.

# This command lists all open files owned by root.

lsof -u root | less

read -p "Hit any key to continue."

############################################################################
echo "########## MOUNT ##########"
# 'mount' is used to mount file systems into the main tree file system.
# This can be useful when adding any external media to your machine.

# This command lists all of the files that are currently mounted.

mount -l | less

read -p "Hit any key to continue."

############################################################################
echo "########## PS ##########"
# 'ps' is used to get information on processes that are currently running,
# canonically used to get PIDs. This tool is incredibly useful when debugging
# rouge / zombie processes.

# This command lists processes associated w/ this terminal and owned by me.

ps -xT | less

read -p "Hit any key to continue."

############################################################################
echo "########## PKILL ##########"
# 'pkill' is used to kill processes without specifying any PIDs. This can be
# useful for quickly killing process that are using a resource without
# having to look up PIDs first.

# This command kills the 'gedit' process.

pkill gedit && echo "Process 'gedit' has been killed"

read -p "Hit any key to continue."

############################################################################
echo "########## NETSTAT ##########"
# 'netstat' is used to view detailed information about network connections.
# This can be useful when needing to see other computers connected to the 
# the network or troubleshooting network issues.

# This command lists all active TCP connections and their corresponding 
# process identifiers. 

netstat -o | less

read -p "Hit any key to continue."

#############################################################################
echo "########## RENICE ##########"
# 'renice' is used to modify the niceness (scheduling priority) of a process
# that's already running.This can be useful if you're having trouble with 
# processes not executing in a specific order.

# This command sets the niceness of hw1.sh to 10

nice -10 ./hw1.sh
ps -lu root | grep hw1.sh

read -p "Hit any key to continue."

############################################################################
echo "########## RSYNC ##########"
# 'rsync' is used to sync a file on a local machine from one location to 
# another. This can be useful when syncing files from local machines to 
# remote machines or servers. 

# The below command syncs/compresses file1.txt to a new folder /test. 

rsync -zvh file1.txt /test

read -p "Hit any key to continue."

############################################################################
echo "########## TIME ##########"
# 'time' is used to see how long a given command takes to run. This can be
# useful when debugging a slow system or outputting detailed reports.

# This command outputs the time taken to download the linux kernel via wget.

time wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.9.tar.gz

read -p "Hit any key to continue."

#############################################################################
echo "########## SSH ##########"
# 'ssh' is used to ensure a secure connection to another host on an insecure
# network. Its useful for having users log onto work machines remotely.

# This command attempts to connect to sample.ssh.com

ssh sample.ssh.com

read -p "Hit any key to continue."

#############################################################################
echo "########## STAT ##########"
# 'stat' is used to check the status of a file or a file system. This can be 
# be useful when you need to see the history of a file or file system. 

# This command lists the status of hw2.sh.

stat hw2.sh

read -p "Hit any key to continue."

#############################################################################
echo "########## STRACE ##########"
# 'strace' is used to troubleshoot and debug programs. You can trace system
# calls made by anyone or specific processes. This can be useful when trying
# to determine the cause of an issue on your system.

# This command lists all of the system calls made by 'ls'.

strace df -h

read -p "Hit any key to continue."

#############################################################################
echo "########## UNAME ##########"
# 'uname' is used to report basic information about a computer's software
# and hardware. This can be useful when needing to upgrade the current 
# version of Linux installed or other programs that are dependent on a specific
# build.

# This command lists the kernel, network host name, version number / release
# level / release date, CPU, hardware platform, and operating system.

uname -a

read -p "Hit any key to continue."

#############################################################################
echo "########## WGET #########"

# 'wget' is used to download files over a network, typically when needing
# to install something from source. This is useful when you need to have a
# install something from source in a specific directory and don't want yum 
# or apt to automatically download and install something.

# This command will get the source file for emacs and download it to the 
# current directory.

wget http://ftp.gnu.org/gnu/emacs/emacs-24.4.tar.gz
