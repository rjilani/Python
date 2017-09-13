__author__ = 'rjilani'

import boto.ec2
import boto.dynamodb

#EC2
conn = boto.ec2.connect_to_region("us-west-2",aws_access_key_id='accessid',aws_secret_access_key='secretkey')

print(conn)

conn.stop_instances(instance_ids=['i-c0087804'])

conn.terminate_instances(instance_ids=['i-c0087804'])

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