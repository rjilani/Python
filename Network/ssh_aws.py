import paramiko
import sys

def main():
    pass

if __name__ == '__main__':
    main()

print "paramiko version " + paramiko.__version__

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect('54.183.19.28', username='ec2-user', key_filename='''./****.pem''')

# stdin, stdout, stderr = ssh.exec_command("uptime;ls -l;ls -l;uptime")
# stdin.flush()
# data = stdout.read().splitlines()
# for line in data:
#     print line
# ssh.close()

def info(trasnsfered, total):
    if trasnsfered == total:
        print ("files completed")
        print (total)
    # print (str(trasnsfered) + ":" + str(total))


def put_file():
    sftp = ssh.open_sftp()
    sftpattr = sftp.put(localpath='./upload/create_ec2.json', remotepath='/home/ec2-user/create_ec2.json', callback=info, confirm=True)
    # print sftpattr.st_size
    # stdin, stdout, stderr = ssh.exec_command("cat /home/ec2-user/test.csv")
    # stdin.flush()
    # data = stdout.read().splitlines()
    # for line in data:
    #     print (line)
    sftp.close()

def get_file():
    sftp = ssh.open_sftp()
    sftp.get(localpath='./download/create_ec2.json', remotepath='/home/ec2-user/create_ec2.json', callback=info)

    sftp.close()


try:
    put_file()
    # get_file()
except Exception, e:
    print str(e)


ssh.close()

