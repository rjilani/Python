__author__ = 'rjilani'
import boto
import boto.ec2
import boto.dynamodb
import sys

#EC2
# conn = boto.ec2.connect_to_region("us-west-2",aws_access_key_id='acesskey',aws_secret_access_key='secretkey')

print boto.Version

# conn.run_instances(
#         'ami-f0091d91',
#         key_name='********',
#         instance_type='t2.micro',
#         security_groups=['securityGroup'])

# print(conn)
#
# reservations = conn.get_all_reservations()
#
# print reservations
#
# instances = reservations[0].instances
# #
# print instances
#
# inst = instances[0]
#
# print inst
#
# print inst.instance_type
#
# print inst.placement
#
# print inst.image_id
#
# print inst.id

# listOfImages = conn.get_all_images()
#
# len(listOfImages)
#
# for images in listOfImages:
#     print images

# conn.stop_instances(instance_ids=['i-934d4257'])
# #
# conn.terminate_instances(instance_ids=['i-934d4257'])

#DynaoDb
# conn = boto.dynamodb.connect_to_region("us-west-2",aws_access_key_id='accessid',aws_secret_access_key='secretkey+')
#
# print(conn.list_tables())
#
# table = conn.get_table('Employee')
#
# print (table)

# item = table.new_item(
#
#     hash_key='104',
#     range_key='Accounting'
# )
#
# item.put()

# item = table.get_item(
#         # Your hash key was 'forum_name'
#         hash_key='105',
#         # Your range key was 'subject'
#         range_key='IT'
#     )
#
# item['Salary']=10000
#
# item.put()
#
# print(item)

# table.delete()
