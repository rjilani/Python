import boto.ec2

#EC2
conn = boto.ec2.connect_to_region("us-west-2",aws_access_key_id='acesskey',aws_secret_access_key='secretkey')

# sg = conn.get_all_security_groups()

# for s in sg:
#     print s

# listOfImages = conn.get_all_images()
#
# len(listOfImages)
#
# for images in listOfImages:
#     print images

# conn.run_instances(
#         'ami-9abea4fb',
#         key_name='********',
#         instance_type='t2.micro',
#         security_groups=['RashidsecurityGroup'])
#
# print(conn)

# get info about reserved instance
reservations = conn.get_all_reservations()

print reservations
for reservation in reservations:

    instances = reservation.instances

    print instances

    inst = instances[0]

    print inst

    print inst.instance_type

    print inst.placement

    print inst.image_id

    print inst.id

#
#     conn.start_instances(instance_ids=[inst.id])
#     conn.stop_instances(instance_ids=[inst.id])
#
# conn.stop_instances(instance_ids=[inst.id])

# conn.terminate_instances(instance_ids=[inst.id])
