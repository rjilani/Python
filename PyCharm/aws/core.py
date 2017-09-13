import botocore.session

session = botocore.session.get_session()
client = session.create_client('ec2', region_name='us-west-2')


for reservation in client.describe_instances()['Reservations']:
    for instance in reservation['Instances']:
        print instance['InstanceId']