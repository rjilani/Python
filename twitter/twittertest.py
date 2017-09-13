import twitter
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config = ConfigParser.ConfigParser()
config.read('./config/config.ini')

api = twitter.Api(consumer_key=config.get('Default','consumer_key'),
                      consumer_secret=config.get('Default','consumer_secret'),
                      access_token_key=config.get('Default','access_token'),
                      access_token_secret=config.get('Default','access_token_secret'))

info = api.VerifyCredentials()

statuses = api.GetUserTimeline(611031539)

text = statuses[1].AsDict().items()[2]
text1,mess = text

print mess
# for i in statuses[0].AsDict().items():
#     print i


users = api.GetFriends()

print ([(u.name,u.location,u.listed_count, u.followers_count, u.time_zone, u.id) for u in users])