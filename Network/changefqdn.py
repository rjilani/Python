from fabric.api import *

env.host_string = 'ec2-54-213-63-42.us-west-2.compute.amazonaws.com'
env.user = 'ec2-user'
env.key_filename = './******.pem'
env.warn_only = True

# def update():
#     """Run `sudo apt-get update`.
#
#     lorem ipsum
#     """
#     output = sudo("python /home/ec2-user/HelloWorld/helloworld.py")
#     return output

def getPs():
    # output = sudo('ps -aef | grep "python" ')
    output = sudo('kill -9 2582')
    return output

def runScipt():
    """Run `sudo apt-get update`.

    lorem ipsum
    """
    output = sudo("python /home/ec2-user/HelloWorld/helloworld.py")
    return output

# def hostname():
#     """Run `hostname`"""
#
#     output = run("curl http://169.254.169.254/latest/meta-data/public-hostname")
#     return output
#
# # output = hostname()
# #
# # print output
#
# def repalceString():
#     """Run `hostname`"""
#
#     output = run("sed -i 's/ec2-[0-9]*-[0-9]*-[0-9]*[0-9]*-[0-9]*.[Aa-zZ]*-[Aa-zZ]*-[0-9]*.[a-z]*.[a-z]*.[a-z]*/ec2-101-10-187-21.us-west-2.compute.amazonaws.com/g' /home/ec2-user/test.txt")
#     return output

# output = runScipt()

output = getPs()

print output
