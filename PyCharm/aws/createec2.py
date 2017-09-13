import boto3
import json

# session = boto3.session.Session(region_name="us-west-2",profile_name='ec2')
#
# client = session.client(service_name='ec2')
#
# print client.describe_images()

session = boto3.Session(profile_name='ec2', region_name="us-west-2")

ec2 = session.resource('ec2')

# ids = ['i-0dc2ccac90c6726fc','i-009e1ef59987de6de']

ids = ['i-0dc2ccac90c6726fc']
#
# ec2.instances.filter(InstanceIds=ids).start()
# ec2.instances.filter(InstanceIds=ids).stop()



instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name',
              'Values': ['pending', 'running', 'rebooting', 'stopping', 'stopped', 'shutting-down', 'terminated']}])

for instance in instances:
    # instance.wait_until_running()
    print(instance.id, instance.instance_type, instance.public_ip_address, instance.public_dns_name, instance.state,
          instance.tags)

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)

# ec2_client = session.client('ec2')
# # print ec2_client.describe_availability_zones()
# # print (json.dumps(ec2_client.describe_security_groups(),sort_keys=True, indent=4))
# # print r.headers
# #print ec2_client.describe_images()
#
# with open('./data/networlacl.json', 'w+') as f:
#     f.write(json.dumps(ec2_client.describe_network_acls(),sort_keys=True, indent=4))
