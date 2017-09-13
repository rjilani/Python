__author__ = 'rjilani'


from boto.s3.connection import S3Connection

conn = S3Connection('accesskey', 'secretkey')

print (conn)

bucket = conn.get_bucket('rashidwordpresscode')

print(bucket)

for key in bucket.list():
    print key.name.encode('utf-8')