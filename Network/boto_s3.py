__author__ = 'rjilani'


from boto.s3.connection import S3Connection

conn = S3Connection('accessid', 'secretkey')

print (conn)

b = conn.get_bucket('photorashid')

print(b)