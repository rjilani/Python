import boto3
import json

session = boto3.Session(profile_name='kinesis', region_name="us-west-2")

client = session.client('kinesis')

# session = boto3.Session(profile_name='kinesis', region_name="us-west-2")
#
# kinesis = session.resource('kinesis')

response = client.list_streams()

# print response

# print type(response)
#
# for k,v in response.items():
#     print k,v

dstream = client.describe_stream(StreamName = 'RashidTestStream')

# print dstream

# print type(dstream)
#
# for k,v in dstream.items():
#     print k,v
#     for k,v in v.items():
#         print k,v

response = client.put_record(StreamName = 'RashidTestStream', Data = 'this is a test', PartitionKey='string')

print (response)

shard_id = 'shardId-000000000000'

#
shardit = client.get_shard_iterator(
    StreamName='RashidTestStream',
    ShardId=shard_id,
    ShardIteratorType='LATEST')["ShardIterator"]

records = client.get_records(
    ShardIterator=shardit,
    Limit=123
)

for k,v in records.items():
    print k,v