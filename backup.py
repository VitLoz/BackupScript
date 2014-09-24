#!/usr/local/bin/python2.7

'''
Script to create and store backups to desired place
and with specified config files

Syntax: python.py /path/with/future/backup/
Output: backup_dd_mm_yyyy.tar.gz
'''

import sys
import os
from datetime import datetime
import shutil

#If no parameter where to store backup then warn and quit
if len(sys.argv) < 2:
    print "ERROR: Please, specify where to store backup!"
    quit()

files = ["/usr/src/sys/amd64/conf/SERVER",
         "/etc/namedb/named.conf",
         "/usr/local/etc/squid/squid.conf",
         "/usr/local/etc/dhcpd.conf",
         "/etc/start_if.re0",
         "/etc/dhclient.conf",
         "/etc/firewall.conf",
         "/etc/sysctl.conf",
         "/etc/rc.conf",
         "/etc/ssh/sshd_config",
         "/etc/hosts"]

#Get current date and time
now = datetime.now()
#Create preffix: "backup_dd_mm_yyyy"
backup_date = ("backup_" + str(now.day) +
                     "_" + str(now.month) + 
                     "_" + str(now.year))

#Get folder where script was launched
os.system("cd " + os.path.dirname(os.path.realpath(__file__)))

#Create folder where to store all config files
os.mkdir(backup_date)

#Copying of desired config files
for bkFile in files:
    shutil.copy(bkFile, backup_date)

#Form archive name for backup
archive_name = backup_date + ".tar.gz"

#Make backup archive 
os.system("tar -czvf " + archive_name + " " + backup_date)

#Get folder where to store backup
destdir = sys.argv[1] 

#Copy backup archive to the desired folder (script parameter) 
shutil.copy(archive_name, destdir)

#Remove folder with copied config files
shutil.rmtree(backup_date)

#Remove copied archive with config files
os.remove(archive_name)
