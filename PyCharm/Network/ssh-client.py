__author__ = 'rjilani'

#-------------------------------------------------------------------------------
# Name:        ssh_client
# Purpose:
#
# Author:      rjilan01
#
# Created:     10/26/2015
# Copyright:   (c) rjilan01 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import paramiko
import sys

def main():
    pass

if __name__ == '__main__':
    main()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = None
fo = None

try:

    f = open("servers.txt", "r")
    fo = open("server_memory_info.txt", "wb")

    for line in f:
        print line
        if '#' in line:
            fo.write(line + "\n")

        if '#' not in line:
            info = line.split(',')
            if (info[4].strip()) == '1':

                try:

                    ssh.connect(info[0], port=int(info[1]), username=info[2], password=info[3].strip())
                    #top = 'top -u ' + info[1] + ' -c -n 1 -b'
                    #print top

                    #stdin, stdout, stderr =  ssh.exec_command("sudo apt-get update")
                    stdin, stdout, stderr =  ssh.exec_command("less /proc/meminfo")
                    #stdin, stdout, stderr =  ssh.exec_command("iostat -c")
                    #stdin, stdout, stderr =  ssh.exec_command("less /proc/cpuinfo") # cpu info nproc,lscpu
                    #stdin, stdout, stderr =  ssh.exec_command("netstat -pt") #all tcp ports at, user au for udp ports, pt for process consuming a port
                    #stdin, stdout, stderr =  ssh.exec_command("vmstat -s")
                    #stdin, stdout, stderr =  ssh.exec_command("df -k") #shows file system disk space usage
                    #stdin, stdout, stderr =  ssh.exec_command("mount") #Show all mounted file systems or use mount -l
                    #stdin, stdout, stderr =  ssh.exec_command("free -m") #to see units in GB use free -g, in mb free -m
                    #stdin, stdout, stderr =  ssh.exec_command("find / -name server.xml")
                    #stdin, stdout, stderr =  ssh.exec_command("locate *-ds.xml") #just like find but faster
                    #stdin, stdout, stderr =  ssh.exec_command("find / -name jboss*.jar")
                    #stdin, stdout, stderr =  ssh.exec_command("cat /apps/foundation/ngtvmgstsb/server/tsb/deploy/tsb-ds.xml")
                    #stdin, stdout, stderr =  ssh.exec_command("find / -name *-ds.xml")
                    #stdin, stdout, stderr =  ssh.exec_command("uname -a")
                    #stdin, stdout, stderr =  ssh.exec_command("uptime")
                    #stdin, stdout, stderr =  ssh.exec_command(top)
                    type(stdin)

                    #print stdout.readlines()

                    li = stdout
                    fo.write(info[0] + "\n")
                    for s in li:
                        print s
                        fo.write(s)
                    fo.write("\n")
                    ssh.close()
                except:
                    ssh.close()
                    print 'Exception happnes in ssh block'
                    print sys.exc_info()[0]

    f.close()
    fo.close()
except:
    if f is not None:
        f.close()
    if fo is not None:
        fo.close()
    print 'Exception happnes in main block'
    print sys.exc_info()[0]
