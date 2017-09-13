import sys

from tweepy import OAuthHandler
from tweepy import Stream
from util.configreader import ConfigReader
from twitterlistner import StdOutListener


tweetstype = 'Default'

if len(sys.argv) == 2:
    tweetstype = sys.argv[1]

configreader = ConfigReader('./config/globals.ini', tweetstype)

# Variables that contains the user credentials to access twitter API
access_token = configreader.access_token
access_token_secret = configreader.access_token_secret
consumer_key = configreader.consumer_key
consumer_secret = configreader.consumer_secret

tagstoparse = configreader.tagstoparse
index = configreader.index_type
doc_type = configreader.doc_type
tags = configreader.searchtags

print (tweetstype)
print (tagstoparse)
print (tags)
print (index)
print (doc_type)


# This handles twitter authentication and the connection to twitter Streaming API
l = StdOutListener(index, doc_type, tags)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

# This line filter twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=tags)
