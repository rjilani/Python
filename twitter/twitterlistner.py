import collections
import json

from textblob import TextBlob
from tweepy.streaming import StreamListener
from util.util import filter_tweets
from util.util import post_tweets


# This is a basic listener that just prints received tweets to stdout and send tweets body to be persisted in elasticsearch.


class StdOutListener(StreamListener):
    Tweets = collections.namedtuple('Tweets', 'timestamp name loc text description followers polarity subjectivity')

    def __init__(self, index, doc_type, tags):
        super(StdOutListener, self).__init__()
        self.index = index
        self.doc_type = doc_type
        self.tags = tags

    # def on_data(self, data):
    #     print data
    #     return True

    def on_error(self, status):
        print (status)

    def on_status(self, status):
        try:
            if hasattr(status, 'retweeted_status') or filter_tweets(status.text, self.tags) == 0:
                # print "Retweeted"
                return

            creatdat = status.created_at
            description = status.user.description
            loc = status.user.location
            text = status.text
            name = status.user.screen_name
            followers = status.user.followers_count

            blob = TextBlob(text)
            sent = blob.sentiment
            polarity = sent.polarity
            subjectivity = sent.subjectivity

            tweets = StdOutListener.Tweets(timestamp=str(creatdat), name=name, loc=loc,
                                           text=text, description=description,
                                           followers=followers,
                                           polarity=polarity, subjectivity=subjectivity)

            tweetbody = json.dumps(tweets._asdict())
            post_tweets(self.index, self.doc_type, tweetbody)
            print (tweetbody)
            print('--------------------------------------------------------------------')
        except Exception, e:
            print (str(e))
