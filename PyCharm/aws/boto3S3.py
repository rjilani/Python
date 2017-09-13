import boto3


# client = boto3.client(
#     's3',
#     aws_access_key_id="acesskey",
#     aws_secret_access_key='secretkey',
# )
#
# s3 = client.list_objects(Bucket='rashidwordpresscode')
#
# print s3


# session = boto3.Session(
#     aws_access_key_id='aaaaaaaaaaaaaaaaaaaaaaaaaaa',
#     aws_secret_access_key='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
# )
#
# s3 = session.resource('s3')

# for bucket in s3.buckets.filter(Param='rashidtest'):
#     print(bucket.name)

# data = open('C:\\Users\\rjilani\\Downloads\\IMG_0104.JPG', 'rb')
# s3.Bucket('rashidtest').put_object(Key='dada2.jpg', Body=data)


# bucket = [(bucket.name) for bucket in s3.buckets.limit(2)]

# print bucket

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

for bucket in s3.buckets.filter(Param='rashidtest'):
    print(bucket.name)

bucket = [(bucket.name) for bucket in s3.buckets.limit(2)]

print bucket